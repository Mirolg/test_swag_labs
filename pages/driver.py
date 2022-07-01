import pytest
from selenium.webdriver import Chrome
import chromedriver_autoinstaller






@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()
    driver = Chrome()
    yield driver
    driver.quit()

