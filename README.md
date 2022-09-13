# Blackbaud Student API

This project is a Python library of functions allowing you to interact with Blackbaud with Selenium webdriver and a little bit of requests. This is one of my "first" public projects I have made.

# For context

For context of a lot of web requests, I love to use Burp Suite not to pentest websites, but to do simple automation. I'm not super efficent, but yeah

# "Breakthroughs"

-> The AuthSvcToken cookie holds the "login key" allowing us to login automatically
-> An old AuthSvcToken cookie can be used to generate a new one (after you edit the cookie, Blackbaud automatically updates it to a new one without signing you out)
-> Deleting the AuthSvcToken invalidates the session and it generates a whole new session
-> AuthSvcToken is valid for the entire session
