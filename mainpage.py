import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By



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
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page(browser):

    assert "Python" in browser.title, 'titel page'

def test_03_assert_button(browser):

    assert browser.find_elements(By.XPATH, '//*[@id="id-search-field"]'), 'Search'
    assert browser.find_elements(By.XPATH, '//*[@id="news"]/a'), 'button News'
    assert browser.find_element(By.CSS_SELECTOR, '#downloads > a'), 'Download'
    assert browser.find_element(By.CSS_SELECTOR, "#documentation > a"), 'Button community'
    assert browser.find_element(By.NAME, 'q'), 'Search'
    assert browser.find_element(By.ID, 'submit'), 'button Go'
    assert browser.find_element(By.CLASS_NAME, 'container'), 'container test python'
    assert browser.find_element(By.CLASS_NAME, 'site-headline'), 'logo python tm'








