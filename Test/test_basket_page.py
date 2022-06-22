import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_swag_labs.pages.login_page import LoginPage
from test_swag_labs.Test.base_test import BaseTest
from test_swag_labs.config.config import TestData


class TestBasket(BaseTest):
    BASKET = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    ITEM = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_ITEM_BUTTON = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

    def test_basket(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.login_page.driver.current_url == TestData.INVENTORY_URL
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(TestBasket.BASKET)).click()
        assert self.login_page.driver.current_url == TestData.BASKET_URL
        item = self.login_page.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(item) < 1
        self.login_page.driver.find_element(By.ID, "continue-shopping").click()
        assert self.login_page.driver.current_url == TestData.INVENTORY_URL
        self.login_page.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(TestBasket.BASKET)).click()
        item = self.login_page.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(item) == 1
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(TestBasket.REMOVE_ITEM_BUTTON)).click()
        item = self.login_page.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(item) < 1






