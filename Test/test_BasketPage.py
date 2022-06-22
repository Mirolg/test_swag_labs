import pytest
from test_swag_labs.Pages.LoginPage import LoginPage
from test_swag_labs.Pages.basketPage import BasketPage
from test_swag_labs.Test.testBase import BaseTest
from test_swag_labs.config.config import TestData


class TestBasket(BaseTest, BasketPage):


    def test_basket(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        self.BasketPage.go_to_basket()
        assert self.LoginPage.driver.current_url == TestData.INVENTORY_URL

