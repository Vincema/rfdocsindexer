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

    Strings Should Be Almost Equal    ${string1}    ${string2}    treshold=${90}

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
    ${external_resources_section}=    Exec BS4    bs4_obj.find("h2", text\=re.compile("${INDEXFILE_EXTRES_TITLE}"))
    ...    bs4_obj=${bs4_obj}
    Should Be True    ${external_resources_section}    msg=External resources section not found in the index file

    [Return]    ${{ $external_resources_section.find_next_sibling() }}

Index File Should Contain The Externals Resources
    [Documentation]    Assert that the external resources section exists and contains
    ...    the specified external resources (dict: {name: url,})
    [Arguments]    ${output_dirpath}    ${expected_external_resources}

    ${bs4_obj__ext_section}=    Index File Should Contain External Resources Section    ${output_dirpath}

    FOR    ${name}    ${url}    IN    &{expected_external_resources}

        ${ext_resource}=    Exec BS4    bs4_obj.find("a", href\=re.compile(url))
        ...    bs4_obj=${bs4_obj__ext_section}    url=${url}

        Should Be True    ${ext_resource}
        ...    msg=External resource link with href "${url}" not found in the external resources section of the index file

        Should Be Equal As Strings    ${ext_resource.string}    ${name}
        ...    msg=Bad name for URL "${url}" (expected "${name}", got "${ext_resource.string}")

    END

Index File Should Contain The Library Section
    [Documentation]    Parse the index file and return the library list section if it exists,
    ...    fail otherwise.
    [Arguments]    ${output_dirpath}

    ${bs4_obj}=    Parse Index File    ${output_dirpath}
    ${liblist_section}=    Exec BS4    bs4_obj.find("h2", text\=re.compile("${INDEXFILE_LIBLIST_TITLE}"))
    ...    bs4_obj=${bs4_obj}
    Should Be True    ${liblist_section}    msg=Library list section not found in the index file

    [Return]    ${{ $liblist_section.find_next_sibling() }}

Index File Should Contain The Library List
    [Documentation]    Assert that the specified library are in the index file and that there is a
    ...    hyperlink to an existing HTML file.
    [Arguments]    ${output_dirpath}    ${expected_library_names}

    ${index_dirpath}=    Join Path    ${TEST_DIR}    ${output_dirpath}

    ${bs4_obj__liblist_section}=    Index File Should Contain The Library Section    ${output_dirpath}

    FOR    ${libname}    IN    @{expected_library_names}

        ${libheader}=    Exec BS4    bs4_obj.find("button", recursive\=True, string\=re.compile(libname))
        ...    bs4_obj=${bs4_obj__liblist_section}    libname=${libname}

        Should Be True    ${libheader}
        ...    msg=Header for library "${libname}" not found in the library list section

        ${libkwlist}=    Exec BS4    bs4_obj__libheader.find_parent("h2").find_next_sibling()
        ...    bs4_obj__libheader=${libheader}

        Should Be True    ${libkwlist}    msg=Error when parsing kw list in index file for library "${libname}"

        # The first link should be a valid link to the HTML documentation
        ${libdoc_link}=    Exec BS4    bs4_obj__libkwlist.find("a", recursive\=True)
        ...    bs4_obj__libkwlist=${libkwlist}

        ${libdoc_path}=    Set Variable    ${libdoc_link}[href]
        ${_}    ${ext}=    Split Extension    ${libdoc_path}

        Should Be Equal As Strings    ${ext}    html    msg=Extension for libdoc should be ".html", got ".${ext}"

        File Should Exist    ${index_dirpath}${/}${libdoc_path}
        ...    msg=Path to libdoc file "${index_dirpath}${/}${libdoc_path}" for library "${libname}" is invalid

        Should Be Equal As Strings    ${libdoc_link.string}    Library documentation
        ...    msg=The string of the link to the HTML libdoc should be literaly "Library documentation"

    END
