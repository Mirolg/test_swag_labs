import pytest
from selenium.webdriver import Chrome
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

