*** Settings ***
Documentation       Keywords to perform operations on generated dirs and files.

Library             OperatingSystem
Resource            testutils.resource

*** Keywords ***
Index File Should Be Identical To The Saved One
    [Documentation]    Compare the content of the index file generated and the saved one.
    [Arguments]    ${output_dirpath}    ${saved_index_filename}

    ${index_filepath}=    Join Path    ${TEST_DIR}    ${output_dirpath}    ${INDEX_FILENAME}
    ${expected_index_filepath}=    Join Path    ${INDEX_FILE_EXAMPLES_PATH}    ${saved_index_filename}

    File Should Exist    ${index_filepath}
    File Should Exist    ${expected_index_filepath}

    ${string1}=    Get File    ${index_filepath}
    ${string2}=    Get File    ${expected_index_filepath}

    Should Be Equal As Strings    ${string1}    ${string2}
    ...    msg=Content of "${index_filepath}" is different from expected content in "${expected_index_filepath}"}

Exec BS4
    [Documentation]    Execute a BeautifulSoup command in python.
    [Arguments]    ${command}    @{}    &{ns}

    ${ret}=    Evaluate    ${command}    modules=bs4    namespace=${ns}
    [Return]    ${ret}

Parse Index File
    [Documentation]    Parse the index file with beautifulsoup and return the BeautifulSoup object.
    [Arguments]    ${output_dirpath}

    ${index_filepath}=    Join Path    ${TEST_DIR}    ${output_dirpath}    ${INDEX_FILENAME}

    ${index_content}=    Get File    ${index_filepath}
    ${bs4_object}=    Exec BS4    bs4.BeautifulSoup(index_content, "html.parser")    index_content=${index_content}

    [Return]    ${bs4_object}

Index File Should Contain External Resources Section
    [Documentation]    Parse the index file and return the external resources section if it exists,
    ...    fail otherwise.
    [Arguments]    ${output_dirpath}

    ${bs4_obj}=    Parse Index File    ${output_dirpath}
    ${external_resources_section}=    Exec BS4    bs4_obj.find("h2", text\=re.compile("External resources"))
    ...    bs4_obj=${bs4_obj}
    Should Be True    ${external_resources_section}    msg=External resources section not found in index file

    [Return]    ${external_resources_section}
