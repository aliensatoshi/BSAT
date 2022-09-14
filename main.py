#PLEASE NOTE THIS FILE IS IN VERY EARLY STAGES.
#THAT MEANS IT IS LIKELY THIS WILL NOT WORK UNTIL LAUNCH.

#import selenium
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#import autoinstaller
import chromedriver_autoinstaller

#import other helpful libraries
import time
import json
import os
import random

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
    os.system("cls")
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
        print("Google Speedbump Detected!")
        os.system("cls")
        driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click() #Click "This is me" on Google Speedbump page
        os.system("cls")
        print("Google Speedbump Bypassed!")


def scrapeData():
    day = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[13]/div[1]/div/div/div/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[2]/div[1]").text
    #delete the junk before the number
    day = day.replace("- Day ", "")
    #get the first character of the string
    day = day[0]
    #convert the string to an integer
    day = int(day)

    global name

    name = driver.find_element(By.XPATH, '//*[@id="account-nav"]/span[1]/span').text;
    
    table_id = driver.find_element(By.XPATH, '//*[@id="accordionSchedules"]')
    rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table

    #generate a random number between 1 and 9999999999999999999
    random_id_num = random.randint(1, 9999999999999999999)

    #open random_id.txt file
    random_id = open("random_id.txt", "r")
    #if random_id is in random_id.txt
    if str(random_id_num) in random_id.read():
        #repeat the process of generating a random number until it is not in random_id.txt
        while str(random_id_num) in random_id.read():
            random_id_num = random.randint(1, 9999999999999999999)
    #add the random_id to random_id.txt
    random_id = open("random_id.txt", "a")
    random_id.write(str(random_id_num) + "\n")
    #close random_id.txt file
    random_id.close()

    #create a new file called schedule.json
    with open('schedule-' + str(random_id_num) + '.json', 'w') as f:
        #create a new array
        schedule = []
        id = -1
        for row in rows: 
            id = id+1

            #create a new dictionary in the schedule array
            schedule.append({})

            # get all the columns with data-heading attribute value as 'Time'    
            time_list = row.find_elements(By.XPATH, ".//td[@data-heading='Time']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for date_and_time in time_list:
                print(date_and_time.text)
                schedule[id]['time'] = date_and_time.text

            # get all the columns with data-heading attribute value as 'Block'    
            block_list = row.find_elements(By.XPATH, ".//td[@data-heading='Block']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for block in block_list:
                print(block.text)
                schedule[id]['block'] = block.text

            # get all the columns with data-heading attribute value as 'Activity'    
            activity_list = row.find_elements(By.XPATH, ".//td[@data-heading='Activity']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for activity in activity_list:
                print(activity.text)
                schedule[id]['activity'] = activity.text

            # get all the columns with data-heading attribute value as 'Contact'    
            contact_list = row.find_elements(By.XPATH, ".//td[@data-heading='Contact']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for contact in contact_list:
                print(contact.text)
                schedule[id]['contact'] = contact.text

            # get all the columns with data-heading attribute value as 'Details'    
            details_list = row.find_elements(By.XPATH, ".//td[@data-heading='Details']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for details in details_list:
                print(details.text)
                schedule[id]['details'] = details.text

            # get all the columns with data-heading attribute value as 'Attendance'    
            att_list = row.find_elements(By.XPATH, ".//td[@data-heading='Attendance']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for att in att_list:
                print(att.text)
                schedule[id]['attendance'] = att.text

        #write the schedule array to the schedule.json file
        json.dump(schedule, f, indent=4)

        driver.close()

        os.system("clear")

def logo():                                                         
    print(" .S_SSSs      sSSs   .S_SSSs    sdSS_SSSSSSbs  ")
    print(".SS~SSSSS    d%%SP  .SS~SSSSS   YSSS~S%SSSSSP  ")
    print("S%S   SSSS  d%S'    S%S   SSSS       S%S       ")
    print("S%S    S%S  S%|     S%S    S%S       S%S       ")
    print("S%S SSSS%P  S&S     S%S SSSS%S       S&S       ")
    print("S&S  SSSY   Y&Ss    S&S  SSS%S       S&S       ")
    print("S&S    S&S  `S&&S   S&S    S&S       S&S       ")
    print("S&S    S&S    `S*S  S&S    S&S       S&S       ")
    print("S*S    S&S     l*S  S*S    S&S       S*S       ")
    print("S*S    S*S    .S*P  S*S    S*S       S*S       ")
    print("S*S SSSSP   sSS*S   S*S    S*S       S*S       ")
    print("S*S  SSY    YSS'    SSS    S*S       S*S       ")
    print("SP                         SP        SP        ")
    print("Y                          Y         Y         ")
    print("")

login()
logo()
print (f"Welcome to BSAT, {name}!")
print("")
print("What would you like to do?")
print("")
print("1. View Schedule")
print("2. View Today's Attendance")
#print("3. View Grades")
#print("4. Calculate GPA")
#print("5. Exit")
print("")
choice = input("Enter your choice: ")

if choice == "1":
    scrapeData()
    #view_schedule()




#items = []

#containers = driver.find_elements_by_xpath('//div[@class="container"]')

#for items in containers:
#    name = items.find_element_by_xpath('//div[@class="name"]')
#    print(name.text)