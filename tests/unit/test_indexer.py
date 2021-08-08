import os
import sys
from pathlib import Path
from stat import S_IREAD
from typing import List

import pytest

from rfdocsindexer.config import Config
from rfdocsindexer.indexer import (
    _create_rflibdata_object_from_libname_or_path,
    _expand_and_filter_filepaths,
    _gen_index_file,
    _generate_libdocs,
    _get_libdoc_from_libname_or_path,
    _get_libs_from_names,
    _get_libs_from_paths,
    _index_external_resources,
    _prepare_output_directories,
    index_documentation,
)
from tests.unit.conftest import LIBRARIES_DIR_EXAMPLES
from tests.unit.testdata import (
    external1,
    external2,
    indexedlib1,
    indexedlib2,
    output_libdocs_html_name,
    output_libdocs_json_name,
    output_libdocs_specs_name,
    output_libdocs_xml_name,
    rflibdata1,
    rflibdata2,
)


@pytest.fixture
def glob_expr_list_will_expand(tmp_path: Path) -> List[str]:
    (tmp_path / "file1.file").write_text("")
    (tmp_path / "file2.file").write_text("")
    (tmp_path / "file3.file").write_text("")
    (tmp_path / "directory").mkdir()
    return [
        os.path.join((tmp_path.resolve()), "file1.file"),
        os.path.join((tmp_path.resolve()), "file2.*"),
        os.path.join((tmp_path.resolve()), "*3.file"),
        os.path.join((tmp_path.resolve()), "*directory"),
    ]


def test_expand_and_filter_filepaths_file_not_found_should_return_empty_list():
    filepath = "wrong_file.file"

    valid_paths = _expand_and_filter_filepaths([filepath])

    assert valid_paths == [], "No file should be found"


def test_expand_and_filter_filepaths_file_not_found_stdout_should_contain_warn(capsys):
    filepath = "wrong_file.file"

    _expand_and_filter_filepaths([filepath])
    assert 'Warning: No file found at path "wrong_file.file"' in capsys.readouterr().out


def test_expand_and_filter_filepaths_file_found(glob_expr_list_will_expand: List[str]):
    valid_paths = _expand_and_filter_filepaths(glob_expr_list_will_expand)

    valid_paths_str = list(map(lambda x: str(x), valid_paths))
    assert len(valid_paths_str) == 3, "3 files should be found"
    assert not any(
        "directory" in x for x in valid_paths_str
    ), "directory should not be returned"
    assert any(
        "file1.file" in x for x in valid_paths_str
    ), "file1.file should be expanded"
    assert any(
        "file2.file" in x for x in valid_paths_str
    ), "file2.file should be expanded"
    assert any(
        "file3.file" in x for x in valid_paths_str
    ), "file3.file should be expanded"
    for path in valid_paths:
        assert Path(path).is_file(), "File should be found"


def test_get_libdoc_from_libname_or_path_from_pathlib_path_no_error():
    libdoc = _get_libdoc_from_libname_or_path(
        LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive" / "lib1.resource"
    )

    assert libdoc.name == "lib1"


def test_get_libdoc_from_libname_or_path_from_str_path_no_error():
    libdoc = _get_libdoc_from_libname_or_path(
        str(
            (
                LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive" / "lib1.resource"
            ).resolve()
        )
    )

    assert libdoc.name == "lib1"


def test_get_libdoc_from_libname_or_path_from_name_no_error():
    sys.path.append(str((LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive").resolve()))
    libdoc = _get_libdoc_from_libname_or_path("LibModule1")

    assert libdoc.name == "LibModule1"


def test_get_libdoc_from_libname_or_path_with_error():
    with pytest.raises(RuntimeError) as raised_err:
        _get_libdoc_from_libname_or_path("BadModuleName")

    assert 'Error generating documentation for library "BadModuleName":' in str(
        raised_err.value
    )


def test_create_rflibdata_object_from_libname_or_path_from_str_path():
    libdata = _create_rflibdata_object_from_libname_or_path(
        (LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive" / "lib1.resource").resolve()
    )
    assert libdata.name == "lib1"
    assert libdata.imported_by == "path"


def test_create_rflibdata_object_from_libname_or_path_from_pathlib_path():
    libdata = _create_rflibdata_object_from_libname_or_path(
        (LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive" / "lib1.resource").resolve()
    )
    assert libdata.name == "lib1"
    assert libdata.imported_by == "path"


def test_create_rflibdata_object_from_libname_or_path_from_name():
    sys.path.append(str((LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive").resolve()))
    libdata = _create_rflibdata_object_from_libname_or_path("LibModule1")

    assert libdata.name == "LibModule1"
    assert libdata.imported_by == "name"


def test_get_libs_from_paths():
    libdir_strpath = (LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive").resolve()
    glob_paths = [os.path.join(libdir_strpath, "lib*.resource")]
    libs = _get_libs_from_paths(glob_paths)

    assert len(libs) == 2, "2 libraries should be found"
    assert any(x.name == "lib2" for x in libs), "lib1 should be returned"
    assert any(x.name == "lib2" for x in libs), "lib2 should be returned"


def test_get_libs_from_name():
    names = ["LibModule1", "LibModule2.LibModule2CustomName", "LibModule3"]
    extra_pythonpath = [
        (LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive").resolve(),
        (LIBRARIES_DIR_EXAMPLES / "libraries_dir_recursive" / "subdir1").resolve(),
    ]
    libs = _get_libs_from_names(names, extra_pythonpath)

    assert len(libs) == 3, "3 libraries should be found"
    assert any(x.name == "LibModule1" for x in libs), "LibModule1 should be returned"
    assert any(
        x.name == "LibModule2.LibModule2CustomName" for x in libs
    ), "LibModule2.LibModule2CustomName should be returned"
    assert any(x.name == "LibModule3" for x in libs), "LibModule3 should be returned"


def test_index_external_resources_no_url_stdout_should_contain_warn(capsys):
    urls = []

    ext_resources = _index_external_resources(urls)

    assert ext_resources == [], "No external resources should be found"
    assert capsys.readouterr().out == "", "Stdout should be empty"


def test_index_external_resources_valid_url():
    urls = ["URL1 | http://url1.com", "http://url2.com"]

    ext_resources = _index_external_resources(urls)

    assert len(ext_resources) == 2, "2 external resources should be found"
    assert any(
        x.url == "http://url1.com" and x.name == "URL1" for x in ext_resources
    ), "URL1 should be returned"
    assert any(
        x.url == "http://url2.com" and x.name == "http://url2.com"
        for x in ext_resources
    ), "URL1 should be returned"


def test_index_external_resources_stdout_should_contain_success(capsys):
    urls = ["URL1 | http://url1.com", "http://url2.com"]

    _index_external_resources(urls)

    assert (
        "Indexed external resources" in capsys.readouterr().out
    ), "Stdout message is incorrect"


def test_index_external_resources_invalid_url():
    urls = ["URL1 http://url1.com"]

    with pytest.raises(RuntimeError) as raised_err:
        _index_external_resources(urls)

    assert 'Url format is invalid for url "URL1 http://url1.com"' in str(
        raised_err.value
    )


def test_index_external_resources_invalid_url_name_sep():
    urls = ["URL1 | abc | http://url1.com"]

    with pytest.raises(RuntimeError) as raised_err:
        _index_external_resources(urls)

    assert 'Url format is invalid for url "URL1 | abc | http://url1.com"' in str(
        raised_err.value
    )


def test_gen_index_file(tmp_path: Path):
    for indexedlib in [indexedlib1, indexedlib2]:
        indexedlib.html_libdoc_path = (
            tmp_path / "html_docs" / f"doc{indexedlib.name}.html"
        )
    _gen_index_file([indexedlib1, indexedlib2], [external1, external2], tmp_path)

    gen_index_path = tmp_path / "index.html"
    assert gen_index_path.is_file(), "index.html should be created"


def test_prepare_output_directories_gen_machine_docs(tmp_path: Path):
    html_dir = tmp_path / output_libdocs_html_name
    xml_dir = tmp_path / output_libdocs_xml_name
    json_dir = tmp_path / output_libdocs_json_name
    spec_dir = tmp_path / output_libdocs_specs_name

    html_dir.mkdir()
    json_dir.mkdir()
    xml_dir.mkdir()

    (html_dir / "subdir").mkdir()
    (html_dir / "subdir" / "subsubdir").mkdir()

    _prepare_output_directories(tmp_path, True)

    assert html_dir.is_dir(), f"{output_libdocs_html_name} should be present"
    assert xml_dir.is_dir(), f"{output_libdocs_xml_name} should be present"
    assert json_dir.is_dir(), f"{output_libdocs_json_name} should be present"
    assert spec_dir.is_dir(), f"{output_libdocs_specs_name} should be created"

    assert not any(
        html_dir.iterdir()
    ), f"{output_libdocs_html_name} html content should be deleted"
    assert not any(json_dir.iterdir()), f"{output_libdocs_xml_name} xml should be empty"
    assert not any(
        xml_dir.iterdir()
    ), f"{output_libdocs_json_name} json should be empty"
    assert not any(spec_dir.iterdir()), f"{output_libdocs_specs_name} should be empty"


def test_prepare_output_directories_no_gen_machine_docs(tmp_path: Path):
    html_dir = tmp_path / output_libdocs_html_name

    _prepare_output_directories(tmp_path, False)

    assert html_dir.is_dir(), f"{output_libdocs_html_name} should be created"

    assert not any(html_dir.iterdir()), f"{output_libdocs_html_name} should be empty"


@pytest.mark.skipif(os.name == "nt", reason="permissions not implemented on Windows")
def test_prepare_output_directories_no_permission(tmp_path: Path):
    outdir = tmp_path / "outdir"
    outdir.mkdir()
    outdir.chmod(S_IREAD)

    with pytest.raises(RuntimeError) as raised_err:
        _prepare_output_directories(outdir, False)

    assert "Error when creating output directories:" in str(raised_err.value)


def test_generate_libdocs_no_lib(tmp_path: Path):
    html_dir = tmp_path / output_libdocs_html_name
    xml_dir = tmp_path / output_libdocs_xml_name
    json_dir = tmp_path / output_libdocs_json_name
    spec_dir = tmp_path / output_libdocs_specs_name

    _generate_libdocs([], True, tmp_path)

    assert html_dir.is_dir(), f"{output_libdocs_html_name} should be created"
    assert xml_dir.is_dir(), f"{output_libdocs_xml_name} should be created"
    assert json_dir.is_dir(), f"{output_libdocs_json_name} should be created"
    assert spec_dir.is_dir(), f"{output_libdocs_specs_name} should be created"


def test_generate_libdocs_files_should_be_created(tmp_path: Path):
    html_dir = tmp_path / output_libdocs_html_name
    xml_dir = tmp_path / output_libdocs_xml_name
    json_dir = tmp_path / output_libdocs_json_name
    spec_dir = tmp_path / output_libdocs_specs_name

    _generate_libdocs([rflibdata1, rflibdata2], True, tmp_path)

    assert html_dir.is_dir(), f"{output_libdocs_html_name} should be created"
    assert xml_dir.is_dir(), f"{output_libdocs_xml_name} should be created"
    assert json_dir.is_dir(), f"{output_libdocs_json_name} should be created"
    assert spec_dir.is_dir(), f"{output_libdocs_specs_name} should be created"

    assert (html_dir / "lib1.html").is_file(), "lib1.html should be created"
    assert (html_dir / "lib2.html").is_file(), "lib2.html should be created"
    assert (xml_dir / "lib1.xml").is_file(), "lib1.xml should be created"
    assert (xml_dir / "lib2.xml").is_file(), "lib2.xml should be created"
    assert (json_dir / "lib1.json").is_file(), "lib1.json should be created"
    assert (json_dir / "lib2.json").is_file(), "lib2.json should be created"
    assert (spec_dir / "lib1.spec").is_file(), "lib1.spec should be created"
    assert (spec_dir / "lib2.spec").is_file(), "lib2.spec should be created"


def test_generate_libdocs_no_machine_docs(tmp_path: Path):
    html_dir = tmp_path / output_libdocs_html_name
    xml_dir = tmp_path / output_libdocs_xml_name
    json_dir = tmp_path / output_libdocs_json_name
    spec_dir = tmp_path / output_libdocs_specs_name

    _generate_libdocs([rflibdata1, rflibdata2], False, tmp_path)

    assert html_dir.is_dir(), f"{output_libdocs_html_name} should be created"
    assert not xml_dir.is_dir(), f"{output_libdocs_xml_name} should not created"
    assert not json_dir.is_dir(), f"{output_libdocs_json_name} should not be created"
    assert not spec_dir.is_dir(), f"{output_libdocs_specs_name} should not be created"

    assert (html_dir / "lib1.html").is_file(), "lib1.html should be created"
    assert (html_dir / "lib2.html").is_file(), "lib2.html should be created"


def test_generate_libdocs_stdout_should_contain_success_msg(tmp_path: Path, capsys):
    _generate_libdocs([rflibdata1, rflibdata2], False, tmp_path)

    stdout = capsys.readouterr()[0]

    assert 'Generated doc for "lib1"' in stdout, "stoud should contain success msg"
    assert 'Generated doc for "lib2"' in stdout, "stoud should contain success msg"


def test_generate_libdocs_should_return_objects(tmp_path: Path):
    generated = _generate_libdocs([rflibdata1, rflibdata2], False, tmp_path)

    assert len(generated) == 2, "should return 2 objects"
    names = [x.name for x in generated]
    assert "lib1" in names, "returned objects list should contain lib1"
    assert "lib2" in names, "returned objects list should contain lib2"


def test_index_documentation_default_config(tmp_path: Path):
    expected_html_docs_list = [
        "BuiltIn.html",
        "Collections.html",
        "DateTime.html",
        "Dialogs.html",
        "OperatingSystem.html",
        "Process.html",
        "Screenshot.html",
        "String.html",
        "Telnet.html",
        "XML.html",
    ]
    expected_url = (
        "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"
    )

    index_file = tmp_path / "index.html"
    html_dir = tmp_path / output_libdocs_html_name

    index_documentation(Config(), tmp_path)

    assert index_file.is_file(), "index.html should be created"

    html_docs_list = [x.name for x in html_dir.iterdir()]

    assert sorted(html_docs_list) == sorted(
        expected_html_docs_list
    ), "the generated docs should be the same as the expected docs"

    assert (
        expected_url in index_file.read_text()
    ), "index.html should contain the RF user guide url"
