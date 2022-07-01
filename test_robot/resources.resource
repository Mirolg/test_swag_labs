*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}                                      https://www.saucedemo.com/
${URL_INVENTORY}                            https://www.saucedemo.com/inventory.html
${LOGIN_INPUT}                              id=user-name
${PASSWORD_INPUT}                           id=password
${USERNAME_LOGIN}                           standard_user
${USERNAME_PASSWORD}                        secret_sauce
${WRONG_USERNAME_LOGIN}                     John
${WRONG_USERNAME_PASSWORD}                  John123
${CASE_SENSITIVE_WRONG_USERNAME_LOGIN}      Standard_user
${BROWSER}                                  chrome
${LOGIN_BUTTON}                             id=login-button
${SELECT_CONTAINER}                         class=product_sort_container
${FIRST_ITEM_IN_INV_PRICE}                  class=inventory_item_price
${GO_TO_BASKET}                             class=shopping_cart_container
${CART_ITEM}                                class=cart_item
${CONTINUE_SHOPPING}                        id=continue-shopping
${ADD_TO_BASKET}                            id=add-to-cart-sauce-labs-backpack
${REMOVE_ITEM}                              id=remove-sauce-labs-backpack