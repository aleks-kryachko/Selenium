import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://www.python.org'


def test_01_status_code():
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'Статус не 200'
def test_02_main_page():
    url = 'http://www.python.org'
    driver = webdriver.Chrome(executable_path=".chromedriver.exe")
    driver = webdriver.Chrome()

    driver.get(url=url)
    assert "Python" in driver.title,'не титульная страница'
    time.sleep(2),

def test_03_assert_button():
    driver = webdriver.Chrome(executable_path=".chromedriver.exe")
    driver = webdriver.Chrome()
    driver.get(url=url)
    assert driver.find_elements(By.XPATH, '//*[@id="id-search-field"]'), 'нет поиска'
    assert driver.find_element(By.CSS_SELECTOR, '#downloads > a'), 'нет Загрузить'
    assert driver.find_element(By.NAME, 'q'), 'поисковая строка'
    assert driver.find_element(By.ID, 'submit'), 'кнопки найти'
    time.sleep(1),
    driver.close()





