import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'http://www.python.org'

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    browser = webdriver.Chrome()
    # browser.set_window_size(1416, 1026)
    browser.maximize_window()
    url = 'http://www.python.org'
    print(browser.get_window_size())
    browser.get(url=url)
    browser.set_page_load_timeout(10) # sets timeout to 10 sec
    yield browser
    browser.quit()


def test_01_status_code():
    url = 'http://www.python.org'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page(browser):

    assert "Python" in browser.title, 'title page'
    assert "Python" in browser.title, 'Download'

def test_03_assert_button(browser):

    assert browser.find_elements(By.XPATH, '//*[@id="id-search-field"]'), 'Search'
    assert browser.find_elements(By.XPATH, '//*[@id="news"]/a'), 'button News'
    assert browser.find_element(By.CSS_SELECTOR, '#downloads > a'), 'Download'
    assert browser.find_element(By.CSS_SELECTOR, "#documentation > a"), 'Button community'
    assert browser.find_element(By.NAME, 'q'), 'Search'
    assert browser.find_element(By.ID, 'submit'), 'button Go'
    assert browser.find_element(By.CLASS_NAME, 'container'), 'container test python'
    assert browser.find_element(By.CLASS_NAME, 'site-headline'), 'logo python tm'

def test_04_check_search(browser):

    browser.find_element(By.NAME, 'q').clear()
    browser.find_element(By.NAME, 'q').send_keys('3.9')
    browser.find_element(By.ID, 'submit').click()
    assert browser.find_element(By.LINK_TEXT, 'Python')

    assert browser.find_element(By.CLASS_NAME, 'site-headline'), 'logo python tm'
    assert browser.find_elements(By.CSS_SELECTOR, '#content > div > section > h2'), 'Search'
    assert browser.find_element(By.NAME, 'q'), 'Search'

    browser.find_element(By.NAME, 'q').clear()
    browser.find_element(By.NAME, 'q').send_keys('python')
    browser.find_element(By.ID, 'submit').send_keys(Keys.ENTER)
    assert browser.find_element(By.LINK_TEXT, 'Python')

    assert browser.find_elements(By.XPATH, '//*[@id="news"]/a'),'block_News'
    assert browser.find_elements(By.CSS_SELECTOR, '#content > div > section > form > h3'), 'block_world_Result'
    assert browser.find_elements(By.CSS_SELECTOR, '#content > div > section > form > ul'), 'url_download'

    browser.find_element(By.NAME, 'q').clear()
    browser.find_element(By.NAME, 'q').send_keys('5682146212221')
    browser.find_element(By.ID, 'submit').send_keys(Keys.ENTER)
    assert browser.find_elements(By.CSS_SELECTOR, '#content > div > section > form > ul > p'), 'Not found'

def test_05_download(browser):
    browser.find_element(By.CSS_SELECTOR, '#downloads > a').click()
    browser.find_element(By.CSS_SELECTOR, '#touchnav-wrapper > header > div > div.header-banner > div > p:nth-child(5) > a:nth-child(1)').click()
    browser.find_element(By.CSS_SELECTOR, '#content > div > section > article > ul > li > a').click()
    browser.find_element(By.CSS_SELECTOR, '#content > div > section > article > table > tbody > tr:nth-child(3) > td:nth-child(1) > a').click()
    time.sleep(8)








