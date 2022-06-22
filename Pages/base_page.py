
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_class):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_class)).click()

    def do_send_keys(self, by_class, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_class)).send_keys(text)

    def get_element_text(self, by_class):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_class))
        return element.text

    def is_enabled(self, by_class):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_class))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
