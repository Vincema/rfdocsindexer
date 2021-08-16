import tempfile
from pathlib import Path

_tmp_dir = Path(tempfile.gettempdir())

# Default cli settings
DEFCLI_OUTPUT_DIRNAME = "rfdocs"

# Default config
DEFCONF = {
    "rfdocsindexer": {
        "library_paths": [],
        "library_names": [],
        "build_machine_readable_libdoc": False,
        "extra_modules_searchpaths": [],
        "include_robotframework_resources": True,
        "external_resources": [],
    }
}

# Paths
TEST_DIR = str(_tmp_dir / "atest-rfdocsindexer")
ASSETS_PATH = Path("tests", "assets").absolute()
LIBRARIES_DIR_EXAMPLES_PATH = ASSETS_PATH / "libraries_dir_examples"

# Values
INDEX_FILENAME = "index.html"
HTML_LIBDOCS_DIRNAME = "libdocs_html"
XML_LIBDOCS_DIRNAME = "libdocs_xml"
JSON_LIBDOCS_DIRNAME = "libdocs_json"
LIBSPECS_DIRNAME = "libspecs"
RF_DEFAULT_LIBRARY_NAMES = [
    "BuiltIn",
    "Collections",
    "DateTime",
    "Dialogs",
    "OperatingSystem",
    "Process",
    "Screenshot",
    "String",
    "Telnet",
    "XML",
]

# Configs
SECTION_NAME = "rfdocsindexer"
CONFIG_GEN_MACHINE_LIBDOCS = {
    SECTION_NAME: {
        "build_machine_readable_libdoc": True,
    }
}
CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES = {
    SECTION_NAME: {
        "library_paths": [
            str(LIBRARIES_DIR_EXAMPLES_PATH / "libraries_dir_recursive" / "lib?.*")
        ],
        "library_names": [
            "LibModule1",
            "LibModule2.LibModule2CustomName",
            "LibModule3",
        ],
        "extra_modules_searchpaths": [
            str(LIBRARIES_DIR_EXAMPLES_PATH / "libraries_dir_recursive" / "subdir1"),
            str(LIBRARIES_DIR_EXAMPLES_PATH / "libraries_dir_recursive"),
        ],
        "build_machine_readable_libdoc": True,
        "include_robotframework_resources": False,
    }
}
