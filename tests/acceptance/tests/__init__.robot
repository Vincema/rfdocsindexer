*** Settings ***
Library         OperatingSystem

Suite Setup     Setup Test Environment

*** Keywords ***
Setup Test Environment
    Create Directory    ${TEST_DIR}
