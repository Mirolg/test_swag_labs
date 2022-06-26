import pytest
from selenium.webdriver.common.by import By
from test_swag_labs.pages.base_page import BasePage
from test_swag_labs.config.test_data import TestData
from test_swag_labs.pages.driver import driver


class BasketPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    BASKET = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_ITEM_BUTTON = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    NAME = "cart_item"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)

    def go_to_basket(self):
        self.click(self.BASKET)

    @property
    def items_in_basket(self):
        item = self.driver.find_elements(By.CLASS_NAME, self.NAME)
        return len(item)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def add_to_basket(self):
        self.click(self.ADD_TO_CART)

    def remove_from_basket(self):
        self.click(self.REMOVE_ITEM_BUTTON)

