*** Settings ***
Library  SeleniumLibrary
Resource    ../resources.resource

*** Keywords ***
Prepare Env
    Set Screenshot Directory        ../screenshots

Open Shop Webpage

    OPEN BROWSER                     ${URL}        ${BROWSER}
    Maximize Browser Window

Open Shop Webpage And Correct Login

    OPEN BROWSER                     ${URL}        ${BROWSER}
    Maximize Browser Window
    Input Text      ${LOGIN_INPUT}       ${USERNAME_LOGIN}
    Input Text      ${PASSWORD_INPUT}    ${USERNAME_PASSWORD}
    Click Button    ${LOGIN_BUTTON}



