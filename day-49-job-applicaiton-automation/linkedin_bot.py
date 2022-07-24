from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Constant Variable(s)
SHORT_WAIT_TIME = 2
LONG_WAIT_TIME = 10
USERNAME = os.environ.get("LINKEDIN_ACCOUNT")
PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

# Access the LinkedIn website
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/")
time.sleep(SHORT_WAIT_TIME)

# Click LinkedIn Sign In button
sign_in = driver.find_element(By.CSS_SELECTOR, "div .btn-secondary-emphasis")
sign_in.click()
time.sleep(SHORT_WAIT_TIME)

# Provide user credentials & then click the sign-in button
user_name = driver.find_element(By.ID, "username")
user_name.send_keys(USERNAME)

user_password = driver.find_element(By.ID, "password")
user_password.send_keys(PASSWORD)

user_login = driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large")
user_login.click()
time.sleep(LONG_WAIT_TIME)

# Graceful logout
user_account = driver.find_element(By.CSS_SELECTOR, "button#ember18")
user_account.click()
time.sleep(SHORT_WAIT_TIME)

# Not working... unable to reach the logout link
user_logout = driver.find_element(By.CSS_SELECTOR, "div#ember20")
user_logout.click()

time.sleep(LONG_WAIT_TIME)
