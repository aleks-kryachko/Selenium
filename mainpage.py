import pytest
import requests
from selenium import webdriver
import time

# driver = webdriver.ChromeOptions()

def test_01_status_code():
    url = 'http://www.python.org'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'Статус не 200'
def test_02_main_page():
    driver = webdriver.Chrome(executable_path=".chromedriver.exe")
    driver = webdriver.Chrome()

    driver.get("http://www.python.org")
    assert "Python" in driver.title
    time.sleep(2)
    driver.close()


