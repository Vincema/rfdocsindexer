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

    Run Command

    Output Dir Structure Should Be Valid
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${DEFCONF}[rfdocsindexer][build_machine_readable_libdoc]
    Libdocs Should Be Generated
    ...    @{RF_DEFAULT_LIBRARY_NAMES}
    ...    check_machine_libdocs=${DEFCONF}[rfdocsindexer][build_machine_readable_libdoc]
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}

Command Should Not Erase The Existing Dir Content
    [Documentation]    Execute command without args with the output dir already existing.
    ...    The content of the directory should not be deleted.
    [Setup]    Create Dir Not Empty    ${DEFCLI_OUTPUT_DIRNAME}

    Run Command

    Output Dir Structure Should Be Valid
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${DEFCONF}[rfdocsindexer][build_machine_readable_libdoc]

Command Should Erase The Existing Subdirs Content
    [Documentation]    Execute command without args with the output dir already existing.
    ...    The content of the subdirectories (where the libdocs are) should be deleted before anything.
    [Setup]    Run Keywords
    ...    Create Fake Outputdir    ${DEFCLI_OUTPUT_DIRNAME}    AND
    ...    Create Configfile    config_dict=${CONFIG_GEN_MACHINE_LIBDOCS}

    Run Command    conf.toml

    Output Dir Structure Should Be Valid
    ...    output_dirname=${DEFCLI_OUTPUT_DIRNAME}
    ...    contains_machine_libdocs=${True}
    Libdocs Should Be Generated
    ...    @{RF_DEFAULT_LIBRARY_NAMES}
    ...    check_machine_libdocs=${True}
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
