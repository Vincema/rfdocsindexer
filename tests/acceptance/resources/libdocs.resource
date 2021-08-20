*** Settings ***
Documentation       Keywords to perform operations on generated dirs and files.

Library             OperatingSystem

*** Keywords ***
Output Dir Should Exist
    [Documentation]    Simple test to check if the output directory exists.
    [Arguments]    ${output_dirname}

    Directory Should Exist    ${TEST_DIR}${/}${output_dirname}
    ...    msg=The output directory "${output_dirname}" should exist in "${TEST_DIR}"

Output Dir Should Contain Index And Libdocs Dirs
    [Documentation]    Check that the index file is created, and the libdocs subdir are created if requested.
    [Arguments]    ${output_dirname}    ${contains_machine_libdocs}

    ${outdir_path}=    Join Path    ${TEST_DIR}    ${output_dirname}

    # Check index file exists
    File Should Exist    ${outdir_path}${/}${INDEX_FILENAME}
    ...    msg=The index file "${INDEX_FILENAME}" should be created in "${outdir_path}"

    # Check libdocs dirs should exist / should not exist
    ${machine_libdocs_dirnames}=    Create List    ${XML_LIBDOCS_DIRNAME}    ${JSON_LIBDOCS_DIRNAME}
    ...    ${LIBSPECS_DIRNAME}
    ${expected_dirnames}=    Create List    ${HTML_LIBDOCS_DIRNAME}
    ${unexpected_dirnames}=    Create List

    IF    ${contains_machine_libdocs}

        Append to List    ${expected_dirnames}    @{machine_libdocs_dirnames}

    ELSE

        Append to List    ${unexpected_dirnames}    @{machine_libdocs_dirnames}

    END

    FOR    ${dirname}    IN    @{expected_dirnames}

        Directory Should Exist    ${outdir_path}${/}${dirname}
        ...    msg=The directory "${dirname}" should be created in "${outdir_path}"

    END

    FOR    ${dirname}    IN    @{unexpected_dirnames}

        Directory Should Not Exist    ${outdir_path}${/}${dirname}
        ...    msg=The directory "${dirname}" should not be created in "${outdir_path}"

    END

Output Dir Structure Should Be Valid
    [Documentation]    Validate the output directory structure.
    ...    The output directory should exist, with an index file,
    ...    and the subdirectories that will contain the libdocs.
    [Arguments]    ${output_dirname}    ${contains_machine_libdocs}

    Output Dir Should Exist    ${output_dirname}
    Output Dir Should Contain Index And Libdocs Dirs    ${output_dirname}    ${contains_machine_libdocs}

Libdocs In Subdir Should Be Generated
    [Documentation]    Assert that the libdocs in the subdir specified with the suffix specified are generated.
    [Arguments]    @{library_names}    ${subdir_path}    ${suffix}

    ${expected_libdocs_files}=    Create List
    FOR    ${library_name}    IN    @{library_names}
        Append To List    ${expected_libdocs_files}    ${library_name}.${suffix}
    END

    ${read_files}=    List Directory    ${subdir_path}
    Lists Should Be Equal    ${read_files}    ${expected_libdocs_files}    ignore_order=${True}
    ...    msg=Files in dir "${subdir_path}" and expected files mismatch

Libdocs Should Be Generated
    [Documentation]    Assert that the libdocs are generated in the corresponding subdir.
    [Arguments]    @{library_names}    ${output_dirname}    ${check_machine_libdocs}

    ${html_subdir_path}=    Join Path    ${TEST_DIR}    ${output_dirname}    ${HTML_LIBDOCS_DIRNAME}
    Libdocs In Subdir Should Be Generated
    ...    @{library_names}
    ...    subdir_path=${html_subdir_path}
    ...    suffix=html

    IF    ${check_machine_libdocs}

        ${xml_subdir_path}=    Join Path    ${TEST_DIR}    ${output_dirname}    ${XML_LIBDOCS_DIRNAME}
        ${json_subdir_path}=    Join Path    ${TEST_DIR}    ${output_dirname}    ${JSON_LIBDOCS_DIRNAME}
        ${spec_subdir_path}=    Join Path    ${TEST_DIR}    ${output_dirname}    ${LIBSPECS_DIRNAME}

        Libdocs In Subdir Should Be Generated
        ...    @{library_names}
        ...    subdir_path=${xml_subdir_path}
        ...    suffix=xml

        Libdocs In Subdir Should Be Generated
        ...    @{library_names}
        ...    subdir_path=${json_subdir_path}
        ...    suffix=json

        Libdocs In Subdir Should Be Generated
        ...    @{library_names}
        ...    subdir_path=${spec_subdir_path}
        ...    suffix=spec

    END

Libdoc Should Be Valid
    [Documentation]    Validate the HTML libdoc by comparing its content with an existing version of the libdocs.
    [Arguments]    ${libdoc_filepath}

    ${libdoc_path}    ${libdoc_name}=    Split Path    ${libdoc_filepath}

    File Should Exist    ${LIBDOC_EXAMPLES_PATH}${/}${libdoc_name}    msg=Unknown libdoc "${libdoc_name}"

    ${expected_libdoc_content}=    Get File    ${LIBDOC_EXAMPLES_PATH}${/}${libdoc_name}
    ${read_libdoc_content}=    Get File    ${libdoc_filepath}

    Strings Should Be Almost Equal    ${expected_libdoc_content}    ${read_libdoc_content}    treshold=${95}
