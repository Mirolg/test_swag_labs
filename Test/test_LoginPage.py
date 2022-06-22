import pytest
from test_swag_labs.Pages.LoginPage import LoginPage
from test_swag_labs.Test.testBase import BaseTest
from test_swag_labs.config.config import TestData


class TestLogin(BaseTest):

    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_correct(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.LoginPage.driver.current_url == TestData.INVENTORY_URL

    def test_incorrect_login_and_password(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.WRONG_USERNAME_LOGIN, TestData.WRONG_USERNAME_PASSWORD)
        assert self.LoginPage.driver.current_url == TestData.URL

    def test_correct_login_and_incorrect_password(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.WRONG_USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.LoginPage.driver.current_url == TestData.URL

    def test_case_sensitive(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.CASE_SENSITIVE_WRONG_USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.LoginPage.driver.current_url == TestData.URL

