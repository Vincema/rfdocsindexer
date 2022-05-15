import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import toml
from pydantic import (
    BaseModel,
    DirectoryPath,
    ValidationError,
    root_validator,
    validator,
)

ROBOTFRAMEWORK_LIBRARY_NAMES = [
    "BuiltIn",
    "Collections",
    "DateTime",
    "OperatingSystem",
    "Process",
    "Screenshot",
    "String",
    "Telnet",
    "XML",
]
ROBOTFRAMEWORK_EXTERNAL_RESOURCES = [
    "User guide | https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"  # noqa: E501
]


class Config(BaseModel):
    """
    Dataclass containing all the config options with their default values.
    """

    library_paths: List[str] = []
    library_names: List[str] = []
    build_machine_readable_libdoc: bool = False
    extra_modules_searchpaths: List[DirectoryPath] = []
    include_robotframework_resources: bool = True
    external_resources: List[str] = []

    class Config:
        extra = "forbid"

    @validator("library_names")
    def library_names_are_module_name(cls, v: List[str]) -> List[str]:
        for name in v:
            if (
                not re.match(r"^[a-zA-Z0-9_.]+$", name)
                or name.startswith(".")
                or name.endswith(".")
                or ".." in name
            ):
                raise ValueError(f"Invalid module name: {name}")
        return v

    @root_validator(skip_on_failure=True)
    def add_rf_resources(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if values.get("include_robotframework_resources"):
            values["library_names"].extend(ROBOTFRAMEWORK_LIBRARY_NAMES)
            values["external_resources"].extend(ROBOTFRAMEWORK_EXTERNAL_RESOURCES)

        return values


def parse_configfile(config_file: Optional[Path]) -> Config:
    """
    Parse the config file (TOML format) and return a Config object.

    Args:
        config_file (pathlib.Path) : Path to the config file.

    Returns:
        (Config) : Config object.

    Raises:
        RuntimeError: If an error is encountered while parsing the config file.
    """
    # Return default config if no config file is provided
    if config_file is None:
        return Config()

    # Parse config file if file is given
    try:
        config_dict = toml.load(config_file)
    except (toml.TomlDecodeError, TypeError, FileNotFoundError) as err:
        raise RuntimeError(f"Decoding error: {err}")

    # Check that the section "rfdocsindexer" exists
    if "rfdocsindexer" not in config_dict:
        raise RuntimeError(
            'The config file does not contain a section named "rfdocsindexer"'
        )

    try:
        if config_dict["rfdocsindexer"]:
            return Config(**config_dict["rfdocsindexer"])
        return Config()
    except ValidationError as err:
        raise RuntimeError(f"Bad configuration: {err}")
