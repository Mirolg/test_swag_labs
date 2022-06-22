from selenium.webdriver.common.by import By
from test_swag_labs.pages.basePage import BasePage
from test_swag_labs.config.config import TestData


class BasketPage(BasePage):
    BASKET = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_ITEM_BUTTON = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    def go_to_basket(self):
        self.do_click(self.BASKET)

    def check_basket(self):
        self.get_element_text()


