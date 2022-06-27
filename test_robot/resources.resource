*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}     https://www.saucedemo.com/
${URL_INVENTORY}        https://www.saucedemo.com/inventory.html
${LOGIN_INPUT}      id=user-name
${PASSWORD_INPUT}       id=password
${USERNAME_LOGIN}    standard_user
${USERNAME_PASSWORD}      secret_sauce
${WRONG_USERNAME_LOGIN}     John
${WRONG_USERNAME_PASSWORD}    John123
${CASE_SENSITIVE_WRONG_USERNAME_LOGIN}    Standard_user
${BROWSER}      chrome
${LOGIN_BUTTON}     id=login-button