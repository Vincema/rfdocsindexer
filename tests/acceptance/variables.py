import os
import tempfile

_tmp_dir = tempfile.gettempdir()

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
TEST_DIR = os.path.abspath(os.path.join(_tmp_dir, "atest-rfdocsindexer"))
ASSETS_PATH = os.path.abspath(os.path.join("tests", "assets"))
CONFIG_FILE_EXAMPLES_PATH = os.path.join(ASSETS_PATH, "config_file_examples")
INDEX_FILE_EXAMPLES_PATH = os.path.join(ASSETS_PATH, "index_file_examples")
LIBRARIES_DIR_EXAMPLES_PATH = os.path.join(ASSETS_PATH, "libraries_dir_examples")
LIBDOC_EXAMPLES_PATH = os.path.join(ASSETS_PATH, "libdoc_examples")

# Values
INDEX_FILENAME = "index.html"
HTML_LIBDOCS_DIRNAME = "libdocs_html"
XML_LIBDOCS_DIRNAME = "libdocs_xml"
JSON_LIBDOCS_DIRNAME = "libdocs_json"
LIBSPECS_DIRNAME = "libspecs"
RF_DEFAULT_EXTERNAL_RESOURCES = {
    "User guide": "https://robotframework.org/robotframework\
/latest/RobotFrameworkUserGuide.html"
}
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
INDEXFILE_EXTRES_TITLE = "External resources"
INDEXFILE_LIBLIST_TITLE = "Imported libraries"

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
            os.path.join(
                LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive", "lib?.*"
            )
        ],
        "library_names": [
            "LibModule1",
            "LibModule2.LibModule2CustomName",
            "LibModule3",
        ],
        "extra_modules_searchpaths": [
            os.path.join(
                LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive", "subdir1"
            ),
            os.path.join(LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive"),
        ],
        "build_machine_readable_libdoc": True,
        "include_robotframework_resources": False,
    }
}
CONFIG_LIBDOCS_2_LIBS_AND_RF_LIBS = {
    SECTION_NAME: {
        "library_paths": [
            os.path.join(
                LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive", "lib1.resource"
            )
        ],
        "library_names": [
            "LibModule1",
        ],
        "extra_modules_searchpaths": [
            os.path.join(LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive"),
        ],
        "build_machine_readable_libdoc": True,
        "include_robotframework_resources": True,
    }
}

CONFIG_LIBDOCS_NO_LIBRARY = {
    SECTION_NAME: {
        "build_machine_readable_libdoc": True,
        "include_robotframework_resources": False,
    }
}

CONFIG_LIBDOCS_NO_EXTERNALS = {
    SECTION_NAME: {
        "include_robotframework_resources": False,
        "external_resources": [],
    }
}

CONFIG_LIBDOCS_INCLUDE_2_EXTERNALS = {
    SECTION_NAME: {
        "include_robotframework_resources": False,
        "external_resources": ["http://test.com", "http://robotframework.org"],
    }
}

CONFIG_INDEX_INCLUDE_ALL_LIBS_FROM_RECURSIVE_DIR = {
    SECTION_NAME: {
        "library_paths": [
            os.path.join(
                LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive", "lib?.*"
            )
        ],
        "library_names": [
            "LibModule1",
            "LibModule2.LibModule2CustomName",
            "LibModule3",
        ],
        "extra_modules_searchpaths": [
            os.path.join(
                LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive", "subdir1"
            ),
            os.path.join(LIBRARIES_DIR_EXAMPLES_PATH, "libraries_dir_recursive"),
        ],
        "build_machine_readable_libdoc": True,
        "include_robotframework_resources": True,
        "external_resources": [
            "RF homepage | https://robotframework.org/",
            "http://example.org",
        ],
    }
}
