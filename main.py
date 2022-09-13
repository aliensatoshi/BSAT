#PLEASE NOTE THIS FILE IS IN VERY EARLY STAGES.
#THAT MEANS IT IS LIKELY THIS WILL NOT WORK UNTIL LAUNCH.

#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#import other helpful libraries
import time
import json

#initialize chromedriver
driver = webdriver.Chrome()

def alert(alert_text):
    print("[!] ", alert_text)

def notice(notice_text):
    print("[*] ", notice_text)

def login():
    #open config.json file
    with open('config.json') as f:
        data = json.load(f)

    #get username and password from config.json
    username = data['username']
    password = data['password']

    driver.get("https://stjohnsprep.myschoolapp.com/app#login")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="Username"]').send_keys(username + Keys.ENTER)
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(username + Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(password + Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    time.sleep(2)
    url = driver.current_url
    
    #if url variable contains speedbump
    if "speedbump" in url:
        alert("Google Speedbump Detected!")
        driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
        note("Google Speedbump Bypassed!")


def scrapeData():
    day = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[13]/div[1]/div/div/div/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]').text()

    print("Scraped Data:")
    print("")
    print("Day: ", day)

login()
scrapeData()

#items = []

#containers = driver.find_elements_by_xpath('//div[@class="container"]')

#for items in containers:
#    name = items.find_element_by_xpath('//div[@class="name"]')
#    print(name.text)