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
import sys

#define global variables
global current_id_num

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

    #remove the line break from name
    name = name.replace("\n", " ")
    
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
                schedule[id]['time'] = date_and_time.text

            # get all the columns with data-heading attribute value as 'Block'    
            block_list = row.find_elements(By.XPATH, ".//td[@data-heading='Block']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for block in block_list:
                schedule[id]['block'] = block.text

            # get all the columns with data-heading attribute value as 'Activity'    
            activity_list = row.find_elements(By.XPATH, ".//td[@data-heading='Activity']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for activity in activity_list:
                schedule[id]['activity'] = activity.text

            # get all the columns with data-heading attribute value as 'Contact'    
            contact_list = row.find_elements(By.XPATH, ".//td[@data-heading='Contact']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for contact in contact_list:
                schedule[id]['contact'] = contact.text

            # get all the columns with data-heading attribute value as 'Details'    
            details_list = row.find_elements(By.XPATH, ".//td[@data-heading='Details']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for details in details_list:
                schedule[id]['details'] = details.text

            # get all the columns with data-heading attribute value as 'Attendance'    
            att_list = row.find_elements(By.XPATH, ".//td[@data-heading='Attendance']")
            #col = row.find_elements(By.TAG_NAME, "td")[1] #note: index start from 0, 1 is col 2
            for att in att_list:
                schedule[id]['attendance'] = att.text

        #write the schedule array to the schedule.json file
        json.dump(schedule, f, indent=4)

        driver.close()

        os.system("cls")

        #create current_id.txt file if it doesnt exist
        if not os.path.exists("current_id.txt"):
            open("current_id.txt", "w").close()
        #if the current_id.txt file exists, delete it
        else:
            os.remove("current_id.txt")

        #write the random_id_num to current_id.txt
        current_id_file = open("current_id.txt", "w")
        current_id_file.write(str(random_id_num))

def view_schedule():
    #open current_id.txt file
    current_id_file = open("current_id.txt", "r")
    #set the file contents to a variable
    current_id_num = current_id_file.read()
    #close current_id.txt file
    current_id_file.close()
    #open the schedule.json file
    with open('schedule-' + str(current_id_num) + '.json') as json_file:
        #read the schedule.json file
        data = json.load(json_file)
        os.system("cls")
        #in the array, print the time, block, activity, contact, details, and attendance for each key
        for p in data:
            #if attendance is Attended, pass
            if p['attendance'] == "Attended":
                pass
            else:
                print('Time: ' + p['time'])
                print('Block: ' + p['block'])
                print('Activity: ' + p['activity'])
                print('Contact: ' + p['contact'])
                print('Details: ' + p['details'])
                print('Attendance: ' + p['attendance'] + '')
                print("")

    print("")
    #Press enter to continue to the main menu
    input("Press enter to continue to the main menu...")
    os.system("cls")

def view_att():
    att = 0
    tardy = 0
    na = 0
    absent = 0

    #open current_id.txt file
    current_id_file = open("current_id.txt", "r")
    #set the file contents to a variable
    current_id_num = current_id_file.read()
    #close current_id.txt file
    current_id_file.close()
    #open the schedule.json file
    with open('schedule-' + str(current_id_num) + '.json') as json_file:
        #read the schedule.json file
        data = json.load(json_file)
        os.system("cls")
        #in the array, print the time, block, activity, contact, details, and attendance for each key
        for p in data:
            #if attendance is Attended, pass
            if p['attendance'] == "Attended":
                att = att + 1
                print('Activity: ' + p['activity'])
                print('Attendance: ' + p['attendance'] + '')
                print("")
            elif p['attendance'] == "Tardy":
                tardy = tardy + 1
                print('Activity: ' + p['activity'])
                print('Attendance: ' + p['attendance'] + '')
                print("")
            elif p['attendance'] == "N/A":
                na = na + 1
                print('Activity: ' + p['activity'])
                print('Attendance: ' + p['attendance'] + '')
                print("")
            elif p['attendance'] == "--":
                upcoming = upcoming + 1
                print('Activity: ' + p['activity'])
                print('Attendance: UPCOMING')
                print("")
            elif p['attendance'] == "Absent":
                absent = absent + 1
                print('Activity: ' + p['activity'])
                print('Attendance: ' + p['attendance'] + '')
                print("")
            else:
                print("Error: Attendance record screwed up. Please try again.")

        print("Today's Attendance Summary:")
        print("")
        #if att is greater than 0
        if att > 0:
            print("Attended: " + str(att))
        #if tardy is greater than 0
        if tardy > 0:
            print("Tardy: " + str(tardy))
        #if na is greater than 0
        if na > 0:
            print("N/A: " + str(na))
        #if absent is greater than 0
        if absent > 0:
            print("Absent: " + str(absent))

        print("")
        #Press enter to continue to the main menu
        input("Press enter to continue to the main menu...")
        os.system("cls")


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

def exit():
    print("Exiting...")
    time.sleep(1)
    os.system("cls")
    sys.exit()

login()
time.sleep(5)
scrapeData()

#repeat forever
while True:
    #logo()
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
        view_schedule()

    elif choice == "2":
        view_att()

    #elif choice == "3":
    #    view_grades()

    #elif choice == "4":
    #    calc_gpa()

    elif choice == "5":
        #open current_id.txt file
        current_id_file = open("current_id.txt", "r")
        #set the file contents to a variable
        current_id_num = current_id_file.read()
        #close current_id.txt file
        current_id_file.close()

        #remove schedule-{current_id_num}.json file
        os.remove("schedule-" + str(current_id_num) + ".json")
        #remove current_id.txt file
        os.remove("current_id.txt")
        exit()