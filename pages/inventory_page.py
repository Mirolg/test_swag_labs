import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.test_data import TestData


class InventoryPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    SELECT_SORT = (By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select')
    INVENTORY_ITEM_PRICE = 'inventory_item_price'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)

    # def get_login_page_title(self, title):
    #     return self.get_title(title)
    #
    # def do_login(self, username, password):
    #     self.do_send_keys(self.USERNAME, username)
    #     self.do_send_keys(self.PASSWORD, password)
    #     self.click(self.LOGIN_BUTTON)

    def select_sort(self, repeat):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SELECT_SORT))
        element.click()
        element.send_keys(Keys.ARROW_DOWN * repeat)
        element.send_keys(Keys.ENTER)

    @property
    def first_item_price(self):
        element = self.driver.find_element(By.CLASS_NAME, 'inventory_item_price')
        return element.text


@pytest.fixture()
def inventory_page(driver) -> InventoryPage:
    page = InventoryPage(driver)
    yield page


