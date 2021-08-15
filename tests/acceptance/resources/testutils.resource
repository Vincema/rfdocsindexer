*** Settings ***
Documentation       Keywords to perform misc tests related operation.

Library             OperatingSystem

*** Keywords ***
Clear Test Dir
    [Documentation]    Clear the test directory recursively.

    Remove Directory    ${TEST_DIR}    recursive=${True}
    Create Directory    ${TEST_DIR}

Create Dir Not Empty
    [Documentation]    Create a dir in the test dir containing files and subdirs with files.
    [Arguments]    ${dirname}

    ${dirpath}=    Join Path    ${TEST_DIR}    ${dirname}

    Create Directory    ${dirpath}
    Create File    ${dirpath}${/}file1.txt
    Create Directory    ${dirpath}${/}subdir1
    Create File    ${dirpath}${/}subdir1${/}file2.txt
