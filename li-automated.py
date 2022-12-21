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

# Function to search for Company Recruiters
def search_company_recruiters(companyName : str) -> None:
    # Initialize a step counter variable
    stepCounter = 1
    # Initialize a driver variable to run Google Chrome
    try:
        driver = webdriver.Chrome()
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('LinkedIn Automation Failed', 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('LinkedIn Automation Begin', 'green'))
        stepCounter += 1


    # Initialize a LinkedIn URL
    url_for_linkedin = 'https://www.linkedin.com/home'

    # Get the URL up and running
    try:
        driver.get(url_for_linkedin)
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('LinkedIn URL Open Unsuccesful', 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('LinkedIn URL Open Succesful', 'green'))
        time.sleep(2)
        stepCounter += 1

    # Find Email and Passcode input field using xpath
    email = driver.find_element("xpath", "//input[@name = 'session_key']")
    passcode = driver.find_element("xpath", "//input[@name = 'session_password']")

    # Get Email and Passcode from a file called AuthKeys.txt
    try:
        userInfo = []
        with open("AuthKeys.txt") as Auth:
            for line in Auth:
                userInfo.append(line.replace('\n', ''))
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Get Email and Passcode From a File Unsuccesful', 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Get Email and Passcode From a File Succesful', 'green'))
        stepCounter += 1

    # Enter Email and Passcode in the input field
    try:
        email.send_keys(userInfo[0])
        passcode.send_keys(userInfo[1])
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Enter Email and Passcode In The Input Field Incomplete', 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Enter Email and Passcode In The Input Field Complete', 'green'))
        time.sleep(2)
        stepCounter += 1

    # Click the Submit Button
    try:
        submit = driver.find_element("xpath", "//button[@type = 'submit']").click()
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Click the Submit Button Incomplete', 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Click the Submit Button Complete', 'green'))
        time.sleep(4)
        stepCounter += 1

    # Search for Company recruiters and press Enter
    try:
        search = driver.find_element("xpath", "//input[@placeholder = 'Search']")
        search.send_keys("University Recruiter @ {}".format(companyName))
        search.send_keys(Keys.ENTER)
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Find and search for {} recruiters Unsuccessful'.format(companyName), 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Find and search for {} recruiters Successful'.format(companyName), 'green'))
        time.sleep(3)
        stepCounter += 1

    # See all People Results
    try:
        all_people = driver.find_element("xpath", "//a[text() = 'See all people results']").click()
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Click to see all people results Incomplete'.format(companyName), 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Click to see all people results Complete'.format(companyName), 'green'))
        time.sleep(3)
        stepCounter += 1


    # Connect, Message and Follow Company Recruiters
    try:
        button_elements = driver.find_elements(By.TAG_NAME, 'button')
        for button in button_elements:
            if button.text == 'Follow':
                button.click()
                time.sleep(1)
            elif button.text == 'Connect':
                button.click()
                time.sleep(2)
                pop_up_buttons = driver.find_elements(By.TAG_NAME, 'button')
                for b in pop_up_buttons:
                    if b.text == 'Send':
                        b.click()
                        time.sleep(1)
                        break
                    elif b.text == 'Other':
                        b.click()
                        time.sleep(3)
                        connect_button = driver.find_element("xpath", "//button[@aria-label = 'Connect']").click()
                        time.sleep(2)
                        send_button = driver.find_element("xpath", "//button[@aria-label = 'Send now']").click()
                        time.sleep(2)
                        break
            elif button.text == 'Message':
                print(colored("Hovered over Message", "yellow"))
                # Fix this message feature
                # button.click()
                # time.sleep(2)
                # return
    except Exception as e:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Connect, Message and Follow for {} recruiters Incomplete'.format(companyName), 'red'))
        print("Step {} Error: {}".format(stepCounter, e))
        driver.quit()
        return
    else:
        print(colored('Step {}:'.format(stepCounter), 'white'), colored('Connect, Message and Follow for {} recruiters Complete'.format(companyName), 'green'))
        time.sleep(3)
        stepCounter += 1

    # Quit the driver
    # Make sure you completely close the session on Mac 
    while True:
        try:
            _ = driver.window_handles
        except Exception as e:
            # print("Step {} Error: {}".format(stepCounter, e))
            break
        time.sleep(1)
    driver.quit()
    print(colored('Step {}:'.format(stepCounter), 'white'), colored('Automation Complete', 'green'))


# Call the search company recruiters function
search_company_recruiters(sys.argv[1])
