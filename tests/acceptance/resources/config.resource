*** Settings ***
Documentation       Keyword to manage configuration from RobotFramework

Library             Collections
Library             OperatingSystem

*** Keywords ***
Convert Dict To TOML Str
    [Documentation]    Take a dictionary and convert it to a TOML string.
    [Arguments]    ${values_dict}

    ${toml_str}=    Evaluate    toml.dumps(${values_dict})    modules=toml

    [Return]    ${toml_str}

Create Configfile
    [Documentation]    Create a configfile from the given arguments.
    ...    The file is created in the test dir and is name "conf.toml".
    [Arguments]    ${config_dict}=&{EMPTY}    ${fill_with_default_values}=${False}

    # Merge dicts if "fill_with_default_values" is true
    ${config_to_create}=    Set Variable If    ${fill_with_default_values}    ${{ {**${config_dict}, **${CONFDEF}} }}
    ...    ${config_dict}

    ${toml_str}=    Convert Dict To TOML Str    ${config_to_create}

    Create File    ${TEST_DIR}${/}conf.toml    ${toml_str}
