import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.quit()

