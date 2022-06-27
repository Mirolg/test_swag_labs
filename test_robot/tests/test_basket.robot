*** Settings ***
Library     SeleniumLibrary
Resource    ../pages/setup.robot
Resource    ../resources.resource
Test Teardown    Close All Browsers


*** Test Cases ***
Test Basket
    Open Shop Webpage And Correct Login
    Click Element                    ${GO_TO_BASKET}
    Element Should Not Be Visible    ${CART_ITEM}
    Click Button                     ${CONTINUE_SHOPPING}
    Click Button                     ${ADD_TO_BASKET}
    Click Element                    ${GO_TO_BASKET}
    Element Should Be Visible        ${CART_ITEM}
    Click Button                     ${REMOVE_ITEM}
    Element Should Not Be Visible    ${CART_ITEM}

