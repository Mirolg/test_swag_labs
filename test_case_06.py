from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_sort_low_to_high_price():
    URL = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    USERNAME_LOGIN = 'standard_user'
    USERNAME_PASSWORD = 'secret_sauce'
    wait = WebDriverWait(driver, 5)
    # Go to the website
    driver.get(URL)
    try:
        # Input a valid username
        username = wait.until(ec.visibility_of_element_located((By.ID, 'user-name')))
        username.send_keys(USERNAME_LOGIN)
        # Input a valid password
        password = wait.until(ec.visibility_of_element_located((By.ID, 'password')))
        password.send_keys(USERNAME_PASSWORD)
        # Press the log in button
        log_in_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        log_in_button.send_keys(Keys.ENTER)
        # Sort price low to high
        sort_item = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'product_sort_container')))
        sort_item.click()
        sort_item.send_keys(Keys.ARROW_DOWN)
        sort_item.send_keys(Keys.ARROW_DOWN)
        sort_item.send_keys(Keys.ENTER)
        # Check price
        first_item = driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
        assert first_item == "$7.99"
        # Close browser
        driver.close()
    except TimeoutError:
        print("Timed out waiting for page to load")
