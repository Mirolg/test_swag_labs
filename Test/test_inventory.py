import pytest
from test_swag_labs.pages.inventory_page import InventoryPage, inventory_page
from test_swag_labs.pages.login_page import LoginPage, login
from test_swag_labs.config.test_data import TestData
from test_swag_labs.pages.driver import driver


class TestInventory:

    def test_sort_price_low_to_high(self, driver, login, inventory_page):
        login.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        inventory_page.select_sort(2)
        assert inventory_page.first_item_price == "$7.99"

    def test_sort_price_high_to_low(self, driver, login, inventory_page):
        login.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        inventory_page.select_sort(3)
        assert inventory_page.first_item_price == "$49.99"

    def test_reverse_alphabet(self, driver, login, inventory_page):
        login.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        inventory_page.select_sort(1)
        assert inventory_page.first_item_price == "$15.99"



