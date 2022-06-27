*** Settings ***
Library  SeleniumLibrary
Resource    ../resources.resource

*** Keywords ***
Open Shop Webpage

    OPEN BROWSER                     ${URL}        ${BROWSER}
    Maximize Browser Window



