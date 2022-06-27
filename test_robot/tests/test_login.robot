*** Settings ***
Library     SeleniumLibrary
Resource    ../pages/setup.robot
Resource    ../resources.resource
Test Teardown    Close All Browsers


*** Test Cases ***
Test login_title
    Open Shop Webpage
    Title Should Be    Swag Labs

Test login_correct
    Open Shop Webpage And Correct Login
    Location Should Be      ${URL_INVENTORY}

Test Incorrect Login And Password
    Open Shop Webpage
    Input Text      ${LOGIN_INPUT}       ${WRONG_USERNAME_LOGIN}
    Input Text      ${PASSWORD_INPUT}    ${WRONG_USERNAME_PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Location Should Be      ${URL}

Test Correct Login And Incorrect Password
    Open Shop Webpage
    Input Text      ${LOGIN_INPUT}       ${USERNAME_LOGIN}
    Input Text      ${PASSWORD_INPUT}    ${WRONG_USERNAME_PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Location Should Be      ${URL}

Test Case Sensitive
    Open Shop Webpage
    Input Text      ${LOGIN_INPUT}       ${CASE_SENSITIVE_WRONG_USERNAME_LOGIN}
    Input Text      ${PASSWORD_INPUT}    ${WRONG_USERNAME_PASSWORD}
    Click Button    ${LOGIN_BUTTON}
    Location Should Be      ${URL}










