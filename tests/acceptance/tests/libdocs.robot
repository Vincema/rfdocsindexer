*** Settings ***
Documentation       Test command excution and libdocs generation

Library             OperatingSystem
Resource            cli.resource
Resource            config.resource
Resource            libdocs.resource
Resource            testutils.resource

Test Teardown       Clear Test Dir

*** Test Cases ***
Command No Args Should Create Libdocs For Default Libs
    [Documentation]    Execute command without args.
    ...    Check that the libdocs are generated for the default libs.
    [Tags]    config_default    config_include_robotframework_resources

    Run Command

    Output Dir Structure Should Be Valid
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${DEFCONF}[${SECTION_NAME}][build_machine_readable_libdoc]
    Libdocs Should Be Generated
    ...    @{RF_DEFAULT_LIBRARY_NAMES}
    ...    check_machine_libdocs=${DEFCONF}[${SECTION_NAME}][build_machine_readable_libdoc]
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}

Command Should Not Erase The Existing Dir Content
    [Documentation]    Execute command without args with the output dir already existing.
    ...    Also tests a custom output dir name.
    ...    The content of the directory should not be deleted.
    [Tags]    config_default    cliconfig_outputdir
    [Setup]    Create Dir Not Empty    custom_outputdir

    Run Command    outputdir=custom_outputdir

    Output Dir Structure Should Be Valid
    ...    output_dirname=custom_outputdir
    ...    contains_machine_libdocs=${DEFCONF}[${SECTION_NAME}][build_machine_readable_libdoc]

    FOR    ${file}    IN    @{CREATE_DIR_NOT_EMPTY__FILES}

        Should Exist    ${TEST_DIR}${/}custom_outputdir${/}${file}
        ...    msg=Content of the output dir should not be deleted ("${file}" missing in "${TEST_DIR}${/}custom_outputdir"")

    END

Command Should Erase The Existing Subdirs Content
    [Documentation]    Execute command without args with the output dir already existing.
    ...    The content of the subdirectories (where the libdocs are) should be deleted before anything.
    [Tags]    config_build_machine_readable_libdoc    cliconfig_configfile
    [Setup]    Run Keywords
    ...    Create Fake Outputdir    ${DEFCLI_OUTPUT_DIRNAME}    AND
    ...    Create Configfile    config_dict=${CONFIG_GEN_MACHINE_LIBDOCS}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Output Dir Structure Should Be Valid
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${True}
    Libdocs Should Be Generated
    ...    @{RF_DEFAULT_LIBRARY_NAMES}
    ...    check_machine_libdocs=${True}
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}

Command With library_paths And library_names Specified Should Generate Libdocs
    [Documentation]    Execute command with library_paths and library_names specified.
    [Tags]    config_library_paths    config_library_names    config_extra_modules_searchpaths    config_include_robotframework_resources    config_build_machine_readable_libdoc    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Output Dir Structure Should Be Valid    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}[${SECTION_NAME}][build_machine_readable_libdoc]

    ${expected_library_names}=    Create List    lib1    lib2    LibModule1    LibModule2.LibModule2CustomName
    ...    LibModule3
    Libdocs Should Be Generated    @{expected_library_names}
    ...    check_machine_libdocs=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}[${SECTION_NAME}][build_machine_readable_libdoc]
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}

Command With No Lib Specified Should Not Return An Error
    [Documentation]    Execute command with no lib specified.
    ...    Check that the output dir structure is valid and that no libdocs was generated.
    [Tags]    config_include_robotframework_resources    config_build_machine_readable_libdoc    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_NO_LIBRARY}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Output Dir Structure Should Be Valid    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${CONFIG_LIBDOCS_NO_LIBRARY}[${SECTION_NAME}][build_machine_readable_libdoc]
    Libdocs Should Be Generated    @{EMPTY}
    ...    check_machine_libdocs=${CONFIG_LIBDOCS_NO_LIBRARY}[${SECTION_NAME}][build_machine_readable_libdoc]
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}

Bad Config File Should Return An Error
    [Documentation]    Run the command with a bad config file and expect an error code and error message.
    [Tags]    error_handling
    [Setup]    Copy File    ${CONFIG_FILE_EXAMPLES_PATH}${/}config_bad_key.toml    ${TEST_DIR}${/}config_bad_key.toml

    ${result}=    Run Command    configfile=config_bad_key.toml
    ...    success_expected=${False}

    Command Should Have Returned With An Error    ${result}

    Stdout Should Be Empty    ${result}
    Stderr Should Match Regex    ${result}    Bad configuration

Success Message Should Be Prompted For Each Generated Libdocs And At The End
    [Documentation]    Run the command with the default config and expect a success message for
    ...    each generated libdoc (default RF libs).
    ...    A single success message should be prompted at the end.
    [Tags]    config_default

    ${result}=    Run Command

    Stderr Should Be Empty    ${result}
    FOR    ${libname}    IN    @{RF_DEFAULT_LIBRARY_NAMES}

        Stdout Should Match Regex    ${result}    🤖 Generated doc for "${libname}"

    END

Success Message Should Be Prompted At The Command End
    [Documentation]    Run the command with the default config and expect a single success message at the end.
    [Tags]    config_default

    ${result}=    Run Command

    Stdout Should Match Regex    ${result}    👍 Successfully generated docs and index in "${DEFCLI_OUTPUT_DIRNAME}"
    Stderr Should Be Empty    ${result}

Success Message After Adding Externals Resources Should Be Prompted
    [Documentation]    Run the command with a config containing 2 externals and expect a success message after adding the external resources.
    [Tags]    config_include_robotframework_resources    config_external_resources    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_INCLUDE_2_EXTERNALS}

    ${result}=    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Stdout Should Contain Success Message After Ext Resources Added    ${result}
    Stderr Should Be Empty    ${result}

Success Message If No Externals Resources Added Should Not Be Prompted
    [Documentation]    Run the command with a config containing no external and expect no success message.
    [Tags]    config_include_robotframework_resources    config_external_resources    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_NO_EXTERNALS}

    ${result}=    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Run Keyword And Expect Error    *    Stdout Should Contain Success Message After Ext Resources Added    ${result}
    Stderr Should Be Empty    ${result}

Libdocs Content Should Be Valid
    [Documentation]    Validate the content for the generated HTML libdocs.
    [Tags]    config_library_paths    config_library_names    config_extra_modules_searchpaths    config_include_robotframework_resources    config_build_machine_readable_libdoc    cliconfig_configfile
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_2_LIBS_AND_RF_LIBS}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Output Dir Structure Should Be Valid    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${CONFIG_LIBDOCS_2_LIBS_AND_RF_LIBS}[${SECTION_NAME}][build_machine_readable_libdoc]

    ${html_libdocs_dirpath}=    Join Path    ${TEST_DIR}    ${DEFCLI_OUTPUT_DIRNAME}    ${HTML_LIBDOCS_DIRNAME}
    Validate Libdocs Content    ${html_libdocs_dirpath}    HTML

    ${xml_libdocs_dirpath}=    Join Path    ${TEST_DIR}    ${DEFCLI_OUTPUT_DIRNAME}    ${XML_LIBDOCS_DIRNAME}
    Validate Libdocs Content    ${xml_libdocs_dirpath}    XML

    ${json_libdocs_dirpath}=    Join Path    ${TEST_DIR}    ${DEFCLI_OUTPUT_DIRNAME}    ${JSON_LIBDOCS_DIRNAME}
    Validate Libdocs Content    ${json_libdocs_dirpath}    JSON

    ${libpecs_dirpath}=    Join Path    ${TEST_DIR}    ${DEFCLI_OUTPUT_DIRNAME}    ${LIBSPECS_DIRNAME}
    Validate Libdocs Content    ${libpecs_dirpath}    SPEC

*** Keywords ***
Stdout Should Contain Success Message After Ext Resources Added
    [Arguments]    ${result}
    Stdout Should Match Regex    ${result}    🌐 Indexed external resources

Validate Libdocs Content
    [Arguments]    ${libdocs_dirpath}    ${format}

    Directory Should Not Be Empty    ${libdocs_dirpath}    msg=${format} libdocs dir should not be empty
    ${libdoc_paths}=    List Files In Directory    ${libdocs_dirpath}    absolute=${True}
    FOR    ${libdoc_path}    IN    @{libdoc_paths}
        Libdoc Should Be Valid    ${libdoc_path}
    END
