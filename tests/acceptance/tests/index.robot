*** Settings ***
Documentation       Test the generated index file

Library             OperatingSystem
Resource            cli.resource
Resource            config.resource
Resource            index.resource
Resource            testutils.resource

Test Teardown       Clear Test Dir

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

    ${expected_resources}=    Create Dictionary
    ...    RF homepage=https://robotframework.org/
    ...    http://example.org=http://example.org
    ...    &{RF_DEFAULT_EXTERNAL_RESOURCES}
    Index File Should Contain The Externals Resources    ${DEFCLI_OUTPUT_DIRNAME}    ${expected_resources}

Index File Should Not Contain The External Resources Section If Empty
    [Documentation]    Assert that the title of the section is not found in the indexfile if
    ...    there is not external resources to show.
    [Tags]    config_external_resources    config_include_robotframework_resources    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_NO_EXTERNALS}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Run Keyword And Expect Error    External resources section not found in the index file
    ...    Index File Should Contain External Resources Section    ${DEFCLI_OUTPUT_DIRNAME}

Index File Should Contain The Library List
    [Documentation]    Assert that the indexfile contains the list of the libraries with
    ...    a link to its corresponding libdoc.
    [Tags]    config_library_paths    config_library_names    config_extra_modules_searchpaths    config_include_robotframework_resources    config_build_machine_readable_libdoc    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    ${expected_library_names}=    Create List    lib1    lib2    LibModule1    LibModule2.LibModule2CustomName
    ...    LibModule3
    Index File Should Contain The Library List    ${DEFCLI_OUTPUT_DIRNAME}    ${expected_library_names}

Index File Should Not Contain The Library List Section If Empty
    [Documentation]    Assert that the title of the section is not found in the indexfile if
    ...    there is not external resourceslibrary to show.
    [Tags]    config_include_robotframework_resources    config_build_machine_readable_libdoc    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_NO_LIBRARY}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Run Keyword And Expect Error    Library list section not found in the index file
    ...    Index File Should Contain The Library Section    ${DEFCLI_OUTPUT_DIRNAME}
