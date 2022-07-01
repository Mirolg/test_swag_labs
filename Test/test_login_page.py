import pytest
from pages.login_page import LoginPage, login
from config.test_data import TestData
from pages.driver import driver


class TestLogin:

    def test_login_page_title(self, driver, login):
        title = login.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_correct(self, driver, login):
        login.do_login(TestData.USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert login.driver.current_url == TestData.INVENTORY_URL

    def test_incorrect_login_and_password(self, driver, login):
        login.do_login(TestData.WRONG_USERNAME_LOGIN, TestData.WRONG_USERNAME_PASSWORD)
        assert login.driver.current_url == TestData.URL

    def test_correct_login_and_incorrect_password(self, driver, login):
        login.do_login(TestData.WRONG_USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert login.driver.current_url == TestData.URL

    def test_case_sensitive(self, driver, login):
        login.do_login(TestData.CASE_SENSITIVE_WRONG_USERNAME_LOGIN, TestData.USERNAME_PASSWORD)
        assert login.driver.current_url == TestData.URL

