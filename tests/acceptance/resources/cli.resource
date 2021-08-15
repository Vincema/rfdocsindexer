*** Settings ***
Documentation       Keywords to run application from CLI

Library             BuiltIn
Library             Collections
Library             Process

*** Keywords ***
Execute CLI
    [Documentation]    Execute the CLI "indexrfdocs". Return the result of the process.
    [Arguments]    @{args}

    ${result}=    Run Process    indexrfdocs    @{args}    cwd=${TEST_DIR}

    [Return]    ${result}

Run Command
    [Documentation]    Run application from CLI. Return the result of the process.
    ...    The configfile and output dir are path relative from the test directory.
    [Arguments]    ${configfile}=${EMPTY}    ${outputdir}=${EMPTY}

    ${args}=    Create List

    IF    "${configfile}"
        Append To List    ${args}    -c    ${TEST_DIR}${/}${configfile}
    END
    IF    "${outputdir}"
        Append To List    ${args}    -o    ${TEST_DIR}${/}${outputdir}
    END
    ${result}=    Execute CLI    @{args}

    [Return]    ${result}
