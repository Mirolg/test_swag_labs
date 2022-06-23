import pytest
from test_swag_labs.pages.inventory_page import InventoryPage
from test_swag_labs.test.base_test import BaseTest
from test_swag_labs.config.config import TestData


class TestInventory(BaseTest):

    def test_inventory(self):
        self.inventory_page = InventoryPage(self.driver)
        self.inventory_page.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        self.inventory_page.sort_price_low_to_high()
        assert self.inventory_page.first_item_price == "$7.99"




