import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
options = webdriver.ChromeOptions()

binary_yandex_driver_file = '.yandexdriver.exe' #for windows
# binary_yandex_driver_file = webdriver.Chrome(executable_path="./usr/local/bin/chromedriver.exe") #for linux
yandex_browser_package_name = 'com.yandex.browser' # Release version of Yandex.Browser
driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
driver.get('https://yandex.ru')
driver.set_page_load_timeout(10) # ждем 10 сек. пока прогрузится страница или найдется элемент
time.sleep(10)
# driver.quit()
