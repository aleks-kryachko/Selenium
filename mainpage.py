import pytest
import requests
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="./chromedriver.exe", )

def test_01_status_code():
    url = 'https://www.ozon.ru/'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'Статус не 200'

print('responce.status_code')

driver.get(url='https://www.ozon.ru/')
#time.sleep(10)
#driver.close()
def __init__(self, browser, url, timeout=10):  # команду для неявного ожидания со значением по умолчанию в 10:
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)

def test_02_open_main_page(self):
    self.browser.get(self.url)
    time.sleep(10)
# def test03_should_be_login_form(self):
