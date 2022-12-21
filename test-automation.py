import sys
import time
import selenium
from datetime import datetime
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
url_for_linkedin = 'https://www.linkedin.com/in/basil-yusuf'

driver.get(url_for_linkedin)

while True:
    try:
        _ = driver.window_handles
    except Exception as e:
        break
    time.sleep(1)
driver.quit()
