*** Settings ***
Documentation       Keywords to perform misc tests related operation.

Library             OperatingSystem
Library             String


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

Create Fake Outputdir
    [Documentation]    Create a fake outputdir.
    [Arguments]    ${dirname}

    Create Dir Not Empty    ${dirname}
    Create Dir Not Empty    ${dirname}${/}${HTML_LIBDOCS_DIRNAME}
    Create Dir Not Empty    ${dirname}${/}${XML_LIBDOCS_DIRNAME}
    Create Dir Not Empty    ${dirname}${/}${JSON_LIBDOCS_DIRNAME}
    Create Dir Not Empty    ${dirname}${/}${LIBSPECS_DIRNAME}

Strings Should Be Almost Equal
    [Documentation]    Uses difflib to compare two strings.
    ...    Raises an error if the similarity ratio is below the given treshold (0-100), default ratio is 90.
    [Arguments]    ${string1}    ${string2}    @{}    ${treshold}=${90}

    ${split_string1}=    Split String    ${string1}
    ${split_string2}=    Split String    ${string2}
    Sort List    ${split_string1}
    Sort List    ${split_string2}

    ${ns}=    Create Dictionary    s1=${split_string1}    s2=${split_string2}
    ${ratio}=    Evaluate    int(difflib.SequenceMatcher(None, s1, s2).ratio() * 100)
    ...    modules=difflib    namespace=${ns}
    Should Be True
    ...    ${ratio} >= ${treshold}
    ...    msg=The two strings are too different (ratio is ${ratio}: below threshold ${treshold})
