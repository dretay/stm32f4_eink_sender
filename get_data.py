print("loading dependencies")
from datetime import datetime
startTime = datetime.now()
import getpass
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import localtime, strftime
from seleniumrequests import Chrome
from seleniumrequests.request import RequestMixin
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
from eink import EInk

eink = EInk()
eink.send_localtime()
eink.send_start()


weather_url = f"https://weather.com/weather/hourbyhour/l/20170:4:US"
print(f"fetching the weather from {weather_url}")
page = urlopen(weather_url)
soup = BeautifulSoup(page, features="html.parser")
hourly_elements = soup.select("table.twc-table tbody tr")

for i, element in enumerate(hourly_elements):    
    time = element.select_one("span.dsx-date").text
    description = element.select_one("td:nth-of-type(3) span").text
    temperature = element.select_one("td:nth-of-type(4) span").text
    eink.send_weather(i, time, description)

print("loading chrome")
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-startup-window")  
chrome_options.add_argument("--bwsi")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-sync")  
chrome_options.add_argument("--disable-background-networking")  
chrome_options.add_argument("--no-first-run")  
chrome_options.add_argument("--aggressive-tab-discard")  
chrome_options.add_argument("--user-agent=Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)")
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')

prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
chrome_options.add_experimental_option("prefs",prefs)

delay = 20 
chrome_options.binary_location = "/usr/bin/chromium-browser"
driver = Chrome(executable_path=os.path.abspath("/usr/lib/chromium-browser/chromedriver"), chrome_options=chrome_options)  
print("logging into outlook")
driver.get("https://outlook.office.com/owa/") 

try:
    driver.find_element_by_name("loginfmt").send_keys("andrew.tayman@fireeye.com")
    driver.find_element_by_id("idSIButton9").click()
    print("entered username, waiting for password prompt")
    

    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'passwordInput')))
        print("password prompt loaded")
    except TimeoutException:
        print("Loading password prompt took too much time!")
        print(driver.page_source)
        driver.close();
        exit(1)

    passwd = getpass.getpass()
    driver.find_element_by_id("passwordInput").send_keys(passwd)
    driver.find_element_by_id("submitButton").click()
    print("entered password, waiting for 2FA token")
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'idSIButton9')))
        driver.find_element_by_id("idSIButton9").click()
        print("asking to remember credentials for next time")
    except TimeoutException:
        print("Loading 2FA page took too much time!")
        print(driver.page_source)
        driver.close();
        exit(1)

    print("2FA accepted, loading office landing page")


except NoSuchElementException:
    print("already logged in")

try:
    print("waiting for landing page to load")
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'lnkBrwsAllFldrs')))
except TimeoutException:
    print(driver.page_source)
    print("Loading landing page too much time!")
    driver.close();
    exit(1)

try:    
    print("loading tasks")
    driver.find_element_by_id("lnkBrwsAllFldrs").click()
    driver.find_element_by_id("selbrfld").click()
    Select(driver.find_element_by_id("selbrfld")).select_by_visible_text("Tasks")
    driver.find_element_by_id("selbrfld").click()
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sent Items'])[1]/following::img[1]").click()    
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'lvw')))
except TimeoutException:
    print(driver.page_source)
    print("Loading todo list took too much time!")
    driver.close();
    exit(1)

elements = driver.find_elements_by_css_selector("td h1 a")
for i, element in enumerate(elements):
    eink.send_todo(i, element.text)    

try:
    print("loading calendar")
    driver.find_element_by_id("lnkNavCal").click()
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'cntnttp')))    
    print("calendar loaded, dumping entries")
except TimeoutException:
    print(driver.page_source)
    print("Loading calendar took too much time!")
    driver.close();
    exit(1)

elements = driver.find_elements_by_css_selector("td.v a")
for i, element in enumerate(elements):    
    eink.send_meeting(i,element.get_attribute('title'))    

total_execution_time = datetime.now() - startTime
print(f"total execution time: {total_execution_time}")

eink.send_flush()
exit(1)
