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
    browser = webdriver.Chrome(executable_path=".chromedriver.exe") #for windows
    # browser = webdriver.Chrome(executable_path="./usr/local/bin/chromedriver.exe") #for linux
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = 'https://www.lambdatest.com/'
    # print(browser.get_window_size())
    browser.get(url=url)
    browser.set_page_load_timeout(10) # sets timeout to 10 sec
    yield browser
    browser.quit()


def test_01_status_code():
    url = 'https://www.lambdatest.com/'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page_for_login(browser):
    assert browser.find_elements(By.XPATH, '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[1]'), 'Login'
    assert browser.find_elements(By.XPATH, '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[2]'), 'Sing Up'
    # browser.find_elements(By.XPATH, '//*[@id="header"]/nav/div/div/div[2]/div/div/div[2]/a[2]').click()

def test_03_Sing_Up_page(browser):
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Login').click()
    # assert browser.find_element(By.PARTIAL_LINK_TEXT, 'google'), 'log_google'
    # assert browser.find_element(By.PARTIAL_LINK_TEXT, 'gitHub'), 'log_gitHub'
    # assert browser.find_element(By.PARTIAL_LINK_TEXT, 'gitHub'), 'log_sso'
    # assert browser.find_element(By.PARTIAL_LINK_TEXT, 'email'), 'email'
    # assert browser.find_element(By.PARTIAL_LINK_TEXT, 'password'), 'password'
    # assert browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div/div/div[1]/div/div[3]/p/span/span[2]/a').click()
    time.sleep(3)

# def test_yandex():
#     binary_yandex_driver_file = '.chromedriver.exe'  # path to YandexDriver
#     driver = webdriver.Chrome('C:/Users/home/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
#     driver.get('https://www.lambdatest.com')
#     # yield driver
#     time.sleep(1)
#     driver.quit()
