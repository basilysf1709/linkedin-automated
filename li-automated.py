from termcolor import colored
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# Initialize a driver variable to run Google Chrome
driver = webdriver.Chrome()
print(colored('Step 1:', 'white'), colored('LinkedIn Automation Begin', 'green'))

# Initialize a LinkedIn URL
url_for_linkedin = 'https://www.linkedin.com/home'

# Get the URL up and running
driver.get(url_for_linkedin)
print(colored('Step 2:', 'white'), colored('LinkedIn URL Open Succesful', 'green'))
time.sleep(2)

# Find Email and Passcode input field using xpath
email = driver.find_element("xpath", "//input[@name = 'session_key']")
passcode = driver.find_element("xpath", "//input[@name = 'session_password']")

userInfo = []
with open("../AuthKeys.txt") as Auth:
    for line in Auth:
        userInfo.append(line)
print(userInfo)

# Enter Email and Passcode in the input field
email.send_keys("My Email")
passcode.send_keys("Some dfasdf")
print(colored('Step 3:', 'white'), colored('Enter Email and Passcode In The Input Field Complete', 'green'))



# Quit the driver
# Make sure you completely close the session on Mac 
while True:
    try:
        _ = driver.window_handles
    except:
        break
    time.sleep(1)
driver.quit()
print(colored('Step:', 'white'), colored('Automation Complete', 'green'))


