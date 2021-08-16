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
    [Arguments]    @{}    ${configfile}=${EMPTY}    ${outputdir}=${EMPTY}    ${success_expected}=${True}

    ${args}=    Create List

    IF    "${configfile}"
        Append To List    ${args}    -c    ${TEST_DIR}${/}${configfile}
    END
    IF    "${outputdir}"
        Append To List    ${args}    -o    ${TEST_DIR}${/}${outputdir}
    END
    ${result}=    Execute CLI    @{args}

    IF    ${success_expected}
        Command Should Have Returned Without Error    ${result}
    END

    [Return]    ${result}

Command Should Have Returned Without Error
    [Documentation]    Check if the rc of the command is 0.
    [Arguments]    ${result}

    Should Be Equal As Integers    0    ${result.rc}    msg=Command result should be 0, got ${result.rc} with stdout "${result.stdout}" and stderr "${result.stderr}"
