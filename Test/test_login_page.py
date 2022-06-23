import pytest
from test_swag_labs.pages.login_page import LoginPage
from test_swag_labs.test.base_test import BaseTest
from test_swag_labs.config.config import TestData


class TestLogin(BaseTest):

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_correct(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.login_page.driver.current_url == TestData.INVENTORY_URL

    def test_incorrect_login_and_password(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.WRONG_USERNAME_LOGIN, TestData.WRONG_USERNAME_PASSWORD)
        assert self.login_page.driver.current_url == TestData.URL

    def test_correct_login_and_incorrect_password(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.WRONG_USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.login_page.driver.current_url == TestData.URL

    def test_case_sensitive(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.CASE_SENSITIVE_WRONG_USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert self.login_page.driver.current_url == TestData.URL

