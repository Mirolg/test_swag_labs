import pytest
from pages.login_page import LoginPage, login
from pages.basket_page import BasketPage
from config.test_data import TestData
from pages.driver import driver


class TestBasket:

    def test_basket(self, login, driver):
        basket_page = BasketPage(driver)
        login.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        basket_page.go_to_basket()
        assert basket_page.driver.current_url == TestData.BASKET_URL
        assert basket_page.items_in_basket < 1
        basket_page.continue_shopping()
        assert basket_page.driver.current_url == TestData.INVENTORY_URL
        basket_page.add_to_basket()
        basket_page.go_to_basket()
        assert basket_page.items_in_basket == 1
        basket_page.remove_from_basket()
        assert basket_page.items_in_basket < 1






