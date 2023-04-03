import requests
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# https://github.com/yandex/YandexDriver/releases

def test_yandex_1():

    options = webdriver.ChromeOptions()

    binary_yandex_driver_file = '.yandexdriver.exe' # path to YandexDriver

    driver = webdriver.Chrome('C:/Users/home/AppData/Local/Yandex/YandexBrowser/Application/browser.exe', options=options)
    # driver = webdriver.Chrome(binary_yandex_driver_file, options=options)

    driver.set_window_size(900, 840)
    driver.set_page_load_timeout(5)
#
    driver.get('https://www.lambdatest.com/')
    time.sleep(5)
    driver.quit()


def test_yandex_2():
    chromeOptions = webdriver.ChromeOptions()
    options = webdriver.ChromeOptions()
    # binary_yandex_driver_file = 'C:/Users/home/PycharmProjects/Selenium/tests/yandexdriver.exe' # path to YandexDriver
    driver = webdriver.Chrome(executable_path=" .yandexdriver.exe")
    driver.quit()
    driver = webdriver.Chrome(r'C:/Users/home/AppData/Local/Yandex/YandexBrowser/Application/browser.exe', options= options);
    driver.set_window_size(900, 800)
    driver.get('https://www.lambdatest.com/')
    # time.sleep(1)
    driver.quit()

def test_yandex_2():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.binary_location =(r"C:/Users/home/AppData/Local/Yandex/YandexBrowser/Application\browser.exe")
    chromeDriver = webdriver.Chrome(executable_path=" .chromeDriver.exe")
    driver = webdriver.Chrome(chromeDriver, options=chromeOptions)
    # driver = webdriver.Chrome(chromeDriver, options=chromeOptions)
    driver.set_window_size(1000, 800)
    driver.get('https://www.lambdatest.com/')
    time.sleep(5)
    driver.quit()
