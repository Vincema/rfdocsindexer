*** Settings ***
Documentation       Test the generated index file

Library             OperatingSystem
Resource            cli.resource
Resource            config.resource
Resource            index.resource
Resource            testutils.resource
# Test Teardown    Clear Test Dir

*** Test Cases ***
Index File Should Be Identical To The One In Tests Assets
    [Documentation]    Assert that the generated index file is identical to the one in the tests assets.
    ...    Non regression test.
    [Tags]    config_library_paths    config_library_names    config_extra_modules_searchpaths    config_include_robotframework_resources    config_build_machine_readable_libdoc    config_external_resources    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_INDEX_INCLUDE_ALL_LIBS_FROM_RECURSIVE_DIR}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Index File Should Be Identical To The Saved One    ${DEFCLI_OUTPUT_DIRNAME}    index_libdir_recursive.html

Index File Should Contain The External Resources
    [Documentation]    Assert that the generated index file contains the external resources.
    [Tags]    config_library_paths    config_library_names    config_extra_modules_searchpaths    config_include_robotframework_resources    config_build_machine_readable_libdoc    config_external_resources    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_INDEX_INCLUDE_ALL_LIBS_FROM_RECURSIVE_DIR}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Index File Should Contain External Resources Section    ${DEFCLI_OUTPUT_DIRNAME}
