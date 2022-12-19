from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


driver = webdriver.Chrome()

url = 'https://linkedin.com/home'

driver.get(url)
time.sleep(3)


driver.quit()