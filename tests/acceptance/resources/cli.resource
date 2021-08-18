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
    ...    The configfile and output dir are path relative to the test directory.
    ...    Fail if `success_expected` is `True` and the process return code is not 0.
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

    Should Be Equal As Integers    0    ${result.rc}
    ...    msg=Command result should be 0, got ${result.rc} with stdout "${result.stdout}" and stderr "${result.stderr}"

Command Should Have Returned With An Error
    [Documentation]    Check if the rc of the command is != 0.
    [Arguments]    ${result}

    Should Not Be Equal As Integers    0    ${result.rc}
    ...    msg=Command result should not be 0, got ${result.rc} with stdout "${result.stdout}" and stderr "${result.stderr}"

Stdout Should Match Regex
    [Documentation]    Check that the stdout matches the given regex.
    [Arguments]    ${result}    ${regex}

    Should Match Regexp    ${result.stdout}    ${regex}    values=${False}
    ...    msg=Stdout "${result.stdout}" should match regex "${regex}"

Stderr Should Match Regex
    [Documentation]    Check that the stderr matches the given regex.
    [Arguments]    ${result}    ${regex}

    Should Match Regexp    ${result.stderr}    ${regex}    values=${False}
    ...    msg=Stderr "${result.stderr}" should match regex "${regex}"

Stdout Should Be Empty
    [Documentation]    Check that the stdout is empty.
    [Arguments]    ${result}

    Should Be Empty    ${result.stdout}    msg=Stdout "${result.stdout}" should be empty

Stderr Should Be Empty
    [Documentation]    Check that the stderr is empty.
    [Arguments]    ${result}

    Should Be Empty    ${result.stderr}    msg=Stderr "${result.stderr}" should be empty
