from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_basket():
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
        # Go to basket
        basket = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        basket.click()
        # Check basket is empty
        item = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(item) < 1
        # Go to inventory
        continue_shopping_button = driver.find_element(By.ID, "continue-shopping")
        continue_shopping_button.click()
        # Add to cart
        add_to_cart = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_to_cart.click()
        # # Go to basket
        basket = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        basket.click()
        # Checking if there is one item in the basket
        item = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(item) == 1
        # Remove item from basket //*[@id="remove-sauce-labs-backpack"]
        remove_button = wait.until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')))
        remove_button.click()
        # Check basket is empty
        item = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(item) < 1
        # Close browser
        driver.close()
    except TimeoutError:
        print("Timed out waiting for page to load")