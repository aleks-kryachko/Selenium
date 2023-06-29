# -*- coding: utf-8 -*-
"""
https://www.chitai-gorod.ru/
проверка корзины добвление удаление

:author: Aleksandr Kryachko
:copyright: Copyright 2023, i'way Selenium Tests
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""
import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
url = 'https://www.chitai-gorod.ru/'

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = 'https://www.chitai-gorod.ru/'
    print(browser.get_window_size())
    browser.get(url=url)
    browser.set_page_load_timeout(10)
    yield browser
    browser.quit()
def test_01_status_code():
    url = 'https://www.chitai-gorod.ru/'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'

def test_02(browser):
    # browser.find_element(By.CLASS_NAME, 'popmechanic-close').click()
    browser.find_element(By.CLASS_NAME, 'header-search__input').send_keys('тестирование')
    # time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'header-search__button-icon').click()
    # assert "Читай-город — интернет-магазин книг" in browser.title
    assert browser.find_element(By.CLASS_NAME, 'products-list')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#__layout > div > div.app-wrapper__content > div.search-page.js-catalog-container > div > div > div > section > section > div > article:nth-child(4) > div.product-buttons.buttons.product-card__controls > div.button.action-button.blue').click()
    browser.find_element(By.CSS_SELECTOR, '#__layout > div > div.app-wrapper__content > div.search-page.js-catalog-container > div > div > div > section > section > div > article:nth-child(3) > div.product-buttons.buttons.product-card__controls > div.button.action-button.blue')
    time.sleep(1)
    browser.find_element(By.LINK_TEXT, 'Купить').click()
    time.sleep(1)
