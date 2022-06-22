import pytest
from test_swag_labs.pages.basket_page import BasketPage
from test_swag_labs.test.base_test import BaseTest
from test_swag_labs.config.config import TestData


class TestBasket(BaseTest):
    def test_basket(self):
        self.basket_page = BasketPage(self.driver)
        self.basket_page.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        self.basket_page.go_to_basket()
        assert self.basket_page.driver.current_url == TestData.BASKET_URL
        assert self.basket_page.check_items_in_basket() < 1
        self.basket_page.continue_shopping()
        assert self.basket_page.driver.current_url == TestData.INVENTORY_URL
        self.basket_page.add_to_basket()
        self.basket_page.go_to_basket()
        assert self.basket_page.check_items_in_basket() == 1
        self.basket_page.remove_from_basket()
        assert self.basket_page.check_items_in_basket() < 1






