*** Settings ***
Library          SeleniumLibrary
Resource         ../pages/setup.robot
Resource         ../resources.resource
Test Teardown    Close All Browsers
Suite Setup     Prepare Env



*** Keywords ***
Prepare Env
    Set Screenshot Directory        ../screenshots


*** Test Cases ***
Test Sort Price Low To High
    Open Shop Webpage And Correct Login
    Select From List By Value    ${SELECT_CONTAINER}              lohi
    Element Text Should Be       ${FIRST_ITEM_IN_INV_PRICE}       $7.99

Test Sort Price High To Low
    Open Shop Webpage And Correct Login
    Select From List By Value    ${SELECT_CONTAINER}              hilo
    Element Text Should Be       ${FIRST_ITEM_IN_INV_PRICE}       $49.99

Test Reverse Alphabet
    Open Shop Webpage And Correct Login
    Select From List By Value    ${SELECT_CONTAINER}              za
    Element Text Should Be       ${FIRST_ITEM_IN_INV_PRICE}       $15.99


