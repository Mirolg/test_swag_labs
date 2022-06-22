import pytest
from selenium import webdriver


@pytest.fixture(params=["Chrome"], scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.close()
