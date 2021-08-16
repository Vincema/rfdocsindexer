*** Settings ***
Documentation       Test libdocs generation

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
    ...    The content of the directory should not be deleted.
    [Tags]    config_default
    [Setup]    Create Dir Not Empty    ${DEFCLI_OUTPUT_DIRNAME}

    Run Command    outputdir=${DEFCLI_OUTPUT_DIRNAME}

    Output Dir Structure Should Be Valid
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${DEFCONF}[${SECTION_NAME}][build_machine_readable_libdoc]

    FOR    ${file}    IN    @{CREATE_DIR_NOT_EMPTY__FILES}

        Should Exist    ${TEST_DIR}${/}${DEFCLI_OUTPUT_DIRNAME}${/}${file}
        ...    msg=Content of the output dir should not be deleted ("${file}" missing in "${TEST_DIR}${/}${DEFCLI_OUTPUT_DIRNAME}"")

    END

Command Should Erase The Existing Subdirs Content
    [Documentation]    Execute command without args with the output dir already existing.
    ...    The content of the subdirectories (where the libdocs are) should be deleted before anything.
    [Tags]    config_build_machine_readable_libdoc
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
    [Tags]    config_library_paths    config_library_names    config_include_robotframework_resources    config_build_machine_readable_libdoc
    [Setup]    Create Configfile    config_dict=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}

    Run Command    configfile=${CREATE_CONFIGFILE__FILENAME}

    Output Dir Structure Should Be Valid    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}[${SECTION_NAME}][build_machine_readable_libdoc]

    ${expected_library_names}=    Create List    lib1    lib2    LibModule1    LibModule2.LibModule2CustomName
    ...    LibModule3
    Libdocs Should Be Generated    @{expected_library_names}
    ...    check_machine_libdocs=${CONFIG_LIBDOCS_FOR_LIBRARY_PATHS_AND_NAMES}[${SECTION_NAME}][build_machine_readable_libdoc]
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}

*** Keywords ***
Create Fake Outputdir
    [Documentation]    Create a fake outputdir.
    [Arguments]    ${dirname}

    Create Dir Not Empty    ${dirname}
    Create Dir Not Empty    ${dirname}${/}${HTML_LIBDOCS_DIRNAME}
    Create Dir Not Empty    ${dirname}${/}${XML_LIBDOCS_DIRNAME}
    Create Dir Not Empty    ${dirname}${/}${JSON_LIBDOCS_DIRNAME}
    Create Dir Not Empty    ${dirname}${/}${LIBSPECS_DIRNAME}
