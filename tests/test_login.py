from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_correct_login():
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
        # Check URL
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        # Close browser
        driver.close()
    except TimeoutError:
        print("Timed out waiting for page to load")


def test_incorrect_login_and_password():
    URL = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    USERNAME_LOGIN = 'John'
    USERNAME_PASSWORD = 'john123'
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
        # Check URL
        assert driver.current_url == "https://www.saucedemo.com/"
        # Close browser
        driver.close()
    except TimeoutError:
        print("Timed out waiting for page to load")


def test_correct_login_and_incorrect_password():
    URL = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    USERNAME_LOGIN = 'standard_user'
    USERNAME_PASSWORD = 'test123'
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
        # Check URL
        assert driver.current_url == "https://www.saucedemo.com/"
        # Close browser
        driver.close()
    except TimeoutError:
        print("Timed out waiting for page to load")


def test_case_sensitive():
    URL = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    USERNAME_LOGIN = 'Standard_user'
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
        # Check URL
        assert driver.current_url == "https://www.saucedemo.com/"
        # Close browser
        driver.close()
    except TimeoutError:
        print("Timed out waiting for page to load")