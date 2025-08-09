import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Firefox()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()

def test_footer_browser(browser):
    browser.get('https://only.digital/')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    wait = WebDriverWait(browser, 10)
    footer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="tel:+7 (495) 740 99 79"]')))
    assert footer is not None

