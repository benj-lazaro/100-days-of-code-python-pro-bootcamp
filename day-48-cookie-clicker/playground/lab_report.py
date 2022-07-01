from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Constant Variable(s)
SHORT_WAIT_TIME = 5
LONG_WAIT_TIME = 10

# Global Variable(s)
dummy_first_name = "Crash"
dummy_last_name = "Dummy"
dummy_email_address = "crash.dummy@test.com"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Target input fields, provide dummy data & then press ENTER key
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys(f"{dummy_first_name}")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys(f"{dummy_last_name}")

email_address = driver.find_element(By.NAME, "email")
email_address.send_keys(f"{dummy_email_address}")
email_address.send_keys(Keys.ENTER)

# Wait then terminate CHrome browser
time.sleep(LONG_WAIT_TIME)
