#PLEASE NOTE THIS FILE IS IN VERY EARLY STAGES.
#THAT MEANS IT IS LIKELY THIS WILL NOT WORK UNTIL LAUNCH.

#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#import autoinstaller
import chromedriver_autoinstaller

#import other helpful libraries
import time
import json

#import os for system and name for clearing and determining what os is being used
import os
from os import system, name

chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--log-level=0")

driver = webdriver.Chrome(service_log_path=os.devnull) #send the log files to nowhere (because I hate the dirty look of it, and it's not needed, but this line can be removed if you want to see the log files)

def login():
    #open config.json file
    with open('config.json') as f:
        data = json.load(f)

    #get username and password from config.json
    username = data['username']
    password = data['password']
    school_url_prefix = data['school_url_prefix']

    driver.get(f"https://{school_url_prefix}.myschoolapp.com/app#login")
    clear()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="Username"]').send_keys(username + Keys.ENTER) #Enter username on Blackbaud email login page
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(username + Keys.ENTER) #Enter username on Microsoft login page
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password + Keys.ENTER) #Enter password on Microsoft login page
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click() #Click "No" on Microsoft "Stay signed in?" page
    time.sleep(2)
    url = driver.current_url
    
    #if url variable contains speedbump
    if "speedbump" in url:
        alert("Google Speedbump Detected!")
        driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click() #Click "This is me" on Google Speedbump page
        notice("Google Speedbump Bypassed!")


def scrapeData():
    day = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[13]/div[1]/div/div/div/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]").text
    #delete the junk before the number
    day = day.replace("- Day ", "")
    #get the first character of the string
    day = day[0]
    #convert the string to an integer
    day = int(day)
    print(day)

    print("Scraped Data:")

login()
time.sleep(5)
scrapeData()

#items = []

#containers = driver.find_elements_by_xpath('//div[@class="container"]')

#for items in containers:
#    name = items.find_element_by_xpath('//div[@class="name"]')
#    print(name.text)