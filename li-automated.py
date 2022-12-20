import time
import selenium
from datetime import datetime
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to search for Company Recruiters
def searchCompanyRecruiters(companyName : str) -> None:
    stepCounter = 1
    # Initialize a driver variable to run Google Chrome
    driver = webdriver.Chrome()
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('LinkedIn Automation Begin', 'green'))
    stepCounter += 1

    # Initialize a LinkedIn URL
    url_for_linkedin = 'https://www.linkedin.com/home'

    # Get the URL up and running
    driver.get(url_for_linkedin)
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('LinkedIn URL Open Succesful', 'green'))
    time.sleep(2)
    stepCounter += 1

    # Find Email and Passcode input field using xpath
    email = driver.find_element("xpath", "//input[@name = 'session_key']")
    passcode = driver.find_element("xpath", "//input[@name = 'session_password']")


    # Get Email and Passcode from a file called AuthKeys.txt
    userInfo = []
    with open("AuthKeys.txt") as Auth:
        for line in Auth:
            userInfo.append(line.replace('\n', ''))
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('Get Email and Passcode From a File', 'green'))
    stepCounter += 1

    # Enter Email and Passcode in the input field
    email.send_keys(userInfo[0])
    passcode.send_keys(userInfo[1])
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('Enter Email and Passcode In The Input Field Complete', 'green'))
    time.sleep(2)
    stepCounter += 1

    # Click the Submit Button
    submit = driver.find_element("xpath", "//button[@type = 'submit']").click()
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('Click the Submit Button Complete', 'green'))
    time.sleep(4)
    stepCounter += 1

    # Search for Company recruiters and press Enter
    search = driver.find_element("xpath", "//input[@placeholder = 'Search']")
    search.send_keys("University Recruiter @ {}".format(companyName))
    search.send_keys(Keys.ENTER)
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('Find and search for {} recruiters'.format(companyName), 'green'))
    time.sleep(3)
    stepCounter += 1

    # Quit the driver
    # Make sure you completely close the session on Mac 
    while True:
        try:
            _ = driver.window_handles
        except:
            break
        time.sleep(1)
    driver.quit()
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('Automation Complete', 'green'))


searchCompanyRecruiters("Google")
