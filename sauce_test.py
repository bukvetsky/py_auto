import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser

def test_login(browser):
    browser.get('https://www.saucedemo.com/')
    username = browser.find_element(By.XPATH, '//*[@id="user-name"]')
    username.click()
    username.send_keys('standard_user')

    password = browser.find_element(By.XPATH, '//*[@id="password"]')
    password.click()
    password.send_keys('secret_sauce')

    login = browser.find_element(By.XPATH, '//*[@id="login-button"]')
    login.click()

