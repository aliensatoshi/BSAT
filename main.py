#PLEASE NOTE THIS FILE IS IN VERY EARLY STAGES.
#THAT MEANS IT IS LIKELY THIS WILL NOT WORK UNTIL LAUNCH.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stjohnsprep.myschoolapp.com/app#login")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="Username"]').send_keys("ahonor25@stjohnsprep.org" + Keys.ENTER)
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys("ahonor25@stjohnsprep.org" + Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys("realGarf1eld!?" + Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
time.sleep(10)

def scrapeData():
    day = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[13]/div[1]/div/div/div/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]').text()

    print("Scraped Data:")
    print("")
    print("Day: ", day)

scrapeData()

#items = []

#containers = driver.find_elements_by_xpath('//div[@class="container"]')

#for items in containers:
#    name = items.find_element_by_xpath('//div[@class="name"]')
#    print(name.text)