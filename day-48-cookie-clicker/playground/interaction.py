from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

SHORT_WAIT_TIME = 5
LONG_WAIT_TIME = 10

# Launch Chrome browser & access target website
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Search and retrieve the current article count
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# Click the targeted element to load the Statistics page
article_count.click()
time.sleep(SHORT_WAIT_TIME)

# Click the 'Main page' to return to previous page
main_page = driver.find_element(By.LINK_TEXT, "Main page")
main_page.click()


# Search and click the 'Content portals' link
content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
content_portals.click()
time.sleep(SHORT_WAIT_TIME)

# Click the 'Main page' to return to previous page
main_page = driver.find_element(By.LINK_TEXT, "Main page")
main_page.click()

# Look for the search bar and type a subject to search
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# Wait until time runs out then terminate Chrome browser
time.sleep(LONG_WAIT_TIME)
