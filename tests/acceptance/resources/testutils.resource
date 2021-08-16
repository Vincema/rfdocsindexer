*** Settings ***
Documentation       Keywords to perform misc tests related operation.

Library             OperatingSystem

*** Variables ***
@{CREATE_DIR_NOT_EMPTY__FILES}=     file1.txt    file2.json    subdir1    subdir2    subdir1${/}file3.txt

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

    FOR    ${file}    IN    @{CREATE_DIR_NOT_EMPTY__FILES}

        ${path}    ${ext}=    Split Extension    ${file}
        IF    "${ext}"
            Create File    ${dirpath}${/}${file}
        ELSE
            Create Directory    ${dirpath}${/}${file}
        END

    END
