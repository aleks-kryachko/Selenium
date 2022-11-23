import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    url = 'http://www.python.org'
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    browser = webdriver.Chrome()
    browser.get(url=url)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

def test_01_status_code():
    url = 'http://www.python.org'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'Статус не 200'
def test_02_main_page(browser):

    assert "Python" in browser.title, 'не титульная страница'

def test_03_assert_button(browser):

    assert browser.find_elements(By.XPATH, '//*[@id="id-search-field"]'), 'нет поиска'
    assert browser.find_element(By.CSS_SELECTOR, '#downloads > a'), 'нет Загрузить'
    assert browser.find_element(By.NAME, 'q'), 'поисковая строка'
    assert browser.find_element(By.ID, 'submit'), 'кнопки найти'






