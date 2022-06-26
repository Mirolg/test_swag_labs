import pytest
from selenium.webdriver.common.by import By
from test_swag_labs.pages.base_page import BasePage
from test_swag_labs.config.config import TestData
from test_swag_labs.pages.driver import driver


class LoginPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)


@pytest.fixture()
def login(driver) -> LoginPage:
    page = LoginPage(driver)
    yield page
