from typing import List
from unittest import mock

import pydantic
import pytest
import toml
from hypothesis import assume, given
from hypothesis import strategies as st

from rfdocsindexer.config import (
    ROBOTFRAMEWORK_EXTERNAL_RESOURCES,
    ROBOTFRAMEWORK_LIBRARY_NAMES,
    Config,
    parse_configfile,
)

# Example config dicts
CONFIG_DICT_OTHER_SECTION = {"section1": {"key1": "value1", "key2": "value2"}}
CONFIG_DICT_VALID_RFDOCSINDEXER_SECTION = {
    "rfdocsindexer": {"library_paths": ["path1", "path2"]}
}
CONFIG_DICT_UNKNOWN_KEY_RFDOCSINDEXER_SECTION = {
    "rfdocsindexer": {"invalidkey": "invalidvalue"}
}
CONFIG_DICT_EMPTY_RFDOCSINDEXER_SECTION = {"rfdocsindexer": None}
CONFIG_DICT_WITHOUT_RFDOCSINDEXER_SECTION = {**CONFIG_DICT_OTHER_SECTION}
CONFIG_DICT_VALID_RFDOCSINDEXER_SECTION = {
    **CONFIG_DICT_OTHER_SECTION,
    **CONFIG_DICT_VALID_RFDOCSINDEXER_SECTION,
}
CONFIG_DICT_INVALID_RFDOCSINDEXER_SECTION = {
    **CONFIG_DICT_OTHER_SECTION,
    **CONFIG_DICT_UNKNOWN_KEY_RFDOCSINDEXER_SECTION,
}


def test_parse_configfile_no_file():
    ret = parse_configfile(None)
    assert ret == Config()


@mock.patch("toml.load")
def test_parse_configfile_decode_error(mocked_toml_load, tmp_path):
    for err in (toml.TomlDecodeError, TypeError, FileNotFoundError):
        mocked_toml_load.side_effect = err

        with pytest.raises(RuntimeError) as raised_err:
            parse_configfile(tmp_path)
        assert "Decoding error: " in str(raised_err.value), "Invalid error message"

        mocked_toml_load.assert_called_once_with(
            tmp_path
        ), "toml.load() not called once or with wrong args"

        mocked_toml_load.reset_mock()


@mock.patch("toml.load", return_value=CONFIG_DICT_WITHOUT_RFDOCSINDEXER_SECTION)
def test_parse_configfile_no_rfdocsindexer_section(mocked_toml_load, tmp_path):
    with pytest.raises(RuntimeError) as raised_err:
        parse_configfile(tmp_path)
    assert 'The config file does not contain a section named "rfdocsindexer"' in str(
        raised_err.value
    ), "Invalid error message"


@mock.patch("toml.load", return_value=CONFIG_DICT_EMPTY_RFDOCSINDEXER_SECTION)
def test_parse_configfile_empty_rfdocsindexer_section(mocked_toml_load, tmp_path):
    ret = parse_configfile(tmp_path)
    assert ret == Config()


@mock.patch("toml.load", return_value=CONFIG_DICT_VALID_RFDOCSINDEXER_SECTION)
def test_parse_configfile_valid_rfdocsindexer_section(mocked_toml_load, tmp_path):
    ret = parse_configfile(tmp_path)
    assert ret == Config(**CONFIG_DICT_VALID_RFDOCSINDEXER_SECTION["rfdocsindexer"])


@mock.patch("toml.load", return_value=CONFIG_DICT_INVALID_RFDOCSINDEXER_SECTION)
def test_parse_configfile_invalid_rfdocsindexer_section(mocked_toml_load, tmp_path):
    with pytest.raises(RuntimeError) as raised_err:
        parse_configfile(tmp_path)
    assert "Bad configuration: " in str(raised_err.value), "Invalid error message"


@given(st.lists(st.from_regex(r"^[a-zA-Z0-9_.]+$")))
def test_config_validator_library_names_are_module_name(val_list: List[str]):
    for val in val_list:
        assume(val != "")
        assume(not val.startswith(".") and not val.endswith(".") and ".." not in val)

    Config(library_names=val_list)


@pytest.mark.parametrize("name", ["abc.", ".def", "hij..klm", "abc!def"])
def test_config_validator_library_names_not_module_name(name):
    with pytest.raises(pydantic.ValidationError) as raised_err:
        Config(library_names=["abc", "def.ghi", "test1", name])
    assert "Invalid module name: " in str(raised_err.value), "Invalid error message"


def test_config_validator_add_rf_resources():
    config_with_rf_resources = Config(
        include_robotframework_resources=True,
        library_names=["abc"],
        external_resources=["http://test.com"],
    )
    for name in ROBOTFRAMEWORK_LIBRARY_NAMES:
        assert (
            config_with_rf_resources.library_names.count(name) == 1
        ), f"{name} is not unique or not found in list"
    for ext_resource in ROBOTFRAMEWORK_EXTERNAL_RESOURCES:
        assert (
            config_with_rf_resources.external_resources.count(ext_resource) == 1
        ), f"{ext_resource} is not unique or not in the list"

    config_without_rf_resources = Config(
        include_robotframework_resources=False,
        library_names=["abc"],
        external_resources=["http://test.com"],
    )
    for name in ROBOTFRAMEWORK_LIBRARY_NAMES:
        assert (
            config_without_rf_resources.library_names.count(name) == 0
        ), f"{name} should not be in the list"
    for ext_resource in ROBOTFRAMEWORK_EXTERNAL_RESOURCES:
        assert (
            config_without_rf_resources.external_resources.count(ext_resource) == 0
        ), f"{ext_resource} should not be in the list"
