from pathlib import Path
from typing import List

import pydantic
import pytest

from rfdocsindexer.config import (
    ROBOTFRAMEWORK_EXTERNAL_RESOURCES,
    ROBOTFRAMEWORK_LIBRARY_NAMES,
    Config,
    parse_configfile,
)

# Example config dicts
OTHER_SECTION = """
[section1]
key1 = "value1"
key2 = "value2"
"""
RFDOCSINDEXER_SECTION = """
[rfdocsindexer]
"""
VALID_KEY = """
library_paths = ["path1", "path2"]
"""
INVALID_KEY = """
invalidkey = "value"
"""
TOML_BAD_KEY_VALUE = """
bad_value = True
"""
CONFIG_WITHOUT_RFDOCSINDEXER_SECTION = OTHER_SECTION
CONFIG_BAD_KEY_VALUE = OTHER_SECTION + TOML_BAD_KEY_VALUE
CONFIG_WITH_EMPTY_RFDOCSINDEXER_SECTION = OTHER_SECTION + RFDOCSINDEXER_SECTION
CONFIG_WITH_RFDOCSINDEXER_SECTION_VALID = (
    CONFIG_WITH_EMPTY_RFDOCSINDEXER_SECTION + VALID_KEY
)
CONFIG_WITH_RFDOCSINDEXER_SECTION_INVALID = (
    CONFIG_WITH_RFDOCSINDEXER_SECTION_VALID + INVALID_KEY
)


def test_parse_configfile_no_file():
    ret = parse_configfile(None)
    assert ret == Config()


def test_parse_configfile_decode_error(tmp_path: Path):
    config_file = tmp_path / "config.toml"
    config_file.write_text(CONFIG_BAD_KEY_VALUE)

    with pytest.raises(RuntimeError) as raised_err:
        parse_configfile(config_file)
    assert "Decoding error:" in str(raised_err.value), "Invalid error message"


def test_parse_configfile_no_rfdocsindexer_section(tmp_path: Path):
    config_file = tmp_path / "config.toml"
    config_file.write_text(CONFIG_WITHOUT_RFDOCSINDEXER_SECTION)

    with pytest.raises(RuntimeError) as raised_err:
        parse_configfile(config_file)
    assert 'The config file does not contain a section named "rfdocsindexer"' in str(
        raised_err.value
    ), "Invalid error message"


def test_parse_configfile_empty_rfdocsindexer_section(tmp_path: Path):
    config_file = tmp_path / "config.toml"
    config_file.write_text(CONFIG_WITH_EMPTY_RFDOCSINDEXER_SECTION)

    ret = parse_configfile(config_file)
    assert ret == Config()


def test_parse_configfile_valid(tmp_path: Path):
    config_file = tmp_path / "config.toml"
    config_file.write_text(CONFIG_WITH_RFDOCSINDEXER_SECTION_VALID)

    ret = parse_configfile(config_file)
    assert ret == Config(library_paths=["path1", "path2"])


def test_parse_configfile_invalid_rfdocsindexer_section(tmp_path: Path):
    config_file = tmp_path / "config.toml"
    config_file.write_text(CONFIG_WITH_RFDOCSINDEXER_SECTION_INVALID)

    with pytest.raises(RuntimeError) as raised_err:
        parse_configfile(config_file)
    assert "Bad configuration: " in str(raised_err.value), "Invalid error message"


@pytest.mark.parametrize("name", ["Ab1", "Ab1.cD2.Ef3"])
def test_config_validator_library_names_are_module_name(name: List[str]):
    Config(library_names=["ABCdef123", name])


@pytest.mark.parametrize("name", ["abc.", ".def", "hij..klm", "abc!def"])
def test_config_validator_library_names_not_module_name(name: str):
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
