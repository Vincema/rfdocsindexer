import io
import sys
from contextlib import redirect_stdout
from functools import partial
from pathlib import Path
from typing import Optional

import click

from .config import parse_configfile
from .indexer import index_documentation

echo_info = partial(click.secho, fg="white")
echo_error = partial(click.secho, fg="red", err=True)
echo_success = partial(click.secho, fg="green")


@click.command()
@click.option(
    "--config-file",
    "-c",
    help="Path to config file, default configuration used if not given",
    type=click.Path(file_okay=True, dir_okay=False, exists=True, path_type=Path),
)
@click.option(
    "--output-dir",
    "-o",
    default=Path("rfdocs"),
    help='Path to output directory, default is "rfdocs"',
    type=click.Path(dir_okay=True, file_okay=False, path_type=Path),
)
def cli(config_file: Optional[Path], output_dir: Path) -> None:
    """
    Generate and store the RobotFramework documentation of a project.
    Please edit the configuration file if needed.
    """
    try:
        config = parse_configfile(config_file)
    except RuntimeError as err:
        echo_error(f"Error: When parsing config file: {err}")
        sys.exit(1)

    try:
        with redirect_stdout(io.StringIO()) as output:
            index_documentation(config, output_dir)
        stdout = output.getvalue()
        if stdout:
            echo_info(stdout.strip("\n"))
    except RuntimeError as err:
        echo_error(
            f"Error: When indexing documentation: {err}",
        )
        sys.exit(1)

    echo_success(f'Successfully generated docs and index in "{output_dir}"')
