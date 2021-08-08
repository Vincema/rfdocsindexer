import os
import shutil
from pathlib import Path
from stat import S_IREAD

import pytest
from click.testing import CliRunner

from rfdocsindexer.cli import cli
from tests.unit.conftest import CONFIG_FILE_EXAMPLES
from tests.unit.testdata import output_libdocs_html_name


@pytest.fixture(autouse=True)
def delete_rfdocs_dir():
    yield
    shutil.rmtree("rfdocs", ignore_errors=True)


def test_cli_config_error():
    config_file = CONFIG_FILE_EXAMPLES / "config_bad_key.toml"

    runner = CliRunner()
    result = runner.invoke(cli, ["-c", str(config_file)])

    assert (
        "Error: When parsing config file:" in result.output
    ), "Incorrect error message"
    assert result.exit_code != 0


@pytest.mark.skipif(os.name == "nt", reason="permissions not implemented on Windows")
def test_cli_doc_gen_error(tmp_path: Path):
    outpath = tmp_path / "outdir"
    outpath.mkdir()
    outpath.chmod(S_IREAD)

    runner = CliRunner()
    result = runner.invoke(cli, ["-o", outpath])

    assert (
        "Error: When indexing documentation:" in result.output
    ), "Incorrect error message"
    assert result.exit_code != 0


def test_cli_no_args_should_print_success():
    runner = CliRunner()
    result = runner.invoke(cli, [])

    output_dirname = "rfdocs"
    assert (
<<<<<<< HEAD
        f'👍 Successfully generated docs and index in "{output_dirname}"'
        in result.output
    ), "Incorrect error message"
=======
        f'Successfully generated docs and index in "{output_dirname}"' in result.output
    ), "Error message incorrect"
>>>>>>> 91a906d... Remove emojis for better support
    assert result.exit_code == 0


def test_cli_no_args_should_generate_default_docs():
    output_path = Path("rfdocs")
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

    index_file = output_path / "index.html"
    html_dir = output_path / output_libdocs_html_name

    runner = CliRunner()
    runner.invoke(cli, [])

    assert index_file.is_file(), "index.html should be created"

    html_docs_list = [x.name for x in html_dir.iterdir()]

    assert output_path.exists(), "Output directory should exist"

    assert sorted(html_docs_list) == sorted(
        expected_html_docs_list
    ), "the generated docs should be the same as the expected docs"

    assert (
        expected_url in index_file.read_text()
    ), "index.html should contain the RF user guide url"
