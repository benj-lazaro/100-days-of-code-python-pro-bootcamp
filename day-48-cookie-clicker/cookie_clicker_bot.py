from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Constant Variable(s)
SHORT_WAIT_TIME = 1
LONG_WAIT_TIME = 10
TIMEOUT = time.time() + 5
FIVE_MINUTES = time.time() + 60*5

# Access the target website
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(LONG_WAIT_TIME)

# Close the web cookie ads
got_it = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
got_it.click()
time.sleep(SHORT_WAIT_TIME)

# Click the preferred language
english_language = driver.find_element(By.CSS_SELECTOR, "div #langSelect-EN")
english_language.click()

big_cookie = driver.find_element(By.ID, "bigCookie")

while True:
    big_cookie.click()

    if time.time() > TIMEOUT:
        pass

    if time.time() > FIVE_MINUTES:
        # cookie_per_second = driver.find_element(By.ID, "cps").text
        # print(cookie_per_second)
        break

time.sleep(LONG_WAIT_TIME)
