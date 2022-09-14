# BSAT
## Blackbaud Student Analyzer Tool

This project is a Blackbaud Student tool to let you interact with Blackbaud with Selenium with CLI interfaces, a Discord bot, and website. If your school or institution uses Blackbaud, this is a must-fork!

# How it works!

- We use Selenium to open up your school's portal page.
- We input your username + password for you
- We login to Microsoft and/or Google to allow SSO to be automated
- We scrape information from your home page
- We archive and store all of that information locally
- You interact with the data via CLI, Discord, or a website (all self hosted!)

# Security

- We don't store any information (logins, cookies, etc)
- Self hosted and you manage everything

# How to self-host!

***WARNING: This repository is in very early stages. My release schedule is to release the CLI, Discord bot, then Website.***

As this *amazing* project is open source and FOSS (Free-and-Open-Source), you can self host it on a server or PC at home!

- First, open up example-config.json and put in your school or institutions url prefix (**example**.myschoolapp.com)
- Select a mode ("discord", "website", or "cli")
- Rename example-config.json to config.json
- Rename example-random_id.txt to random_id.txt
- Install Python (If you don't already have it)
- Install selenium and chromedriver_autoinstaller (If you don't know how to, open CMD and type "pip install {module to install}" and press enter)
- Run the program with "python main.py" in CMD.

***If you just want to use BSAT, this is not for you!***