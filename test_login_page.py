import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://www.lambdatest.com/'

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    browser = webdriver.Chrome()
    # browser.set_window_size(1416, 1026)
    browser.maximize_window()
    url = 'https://www.lambdatest.com/'
    print(browser.get_window_size())
    browser.get(url=url)
    browser.set_page_load_timeout(10) # sets timeout to 10 sec
    yield browser
    browser.quit()


def test_01_status_code():
    url = 'https://www.lambdatest.com/'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page(browser):
    assert browser.find_elements(By.XPATH, '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[1]'), 'Login'
    assert browser.find_elements(By.XPATH, '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[2]'), 'Sing Up'

