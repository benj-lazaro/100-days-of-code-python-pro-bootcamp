from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Constant Variable(s)
SHORT_WAIT_TIME = 1
LONG_WAIT_TIME = 10
TIMEOUT = time.time() + 7
FIVE_MINUTES = time.time() + 60*5

# Access the target website
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
time.sleep(SHORT_WAIT_TIME)

web_cookie_button = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
web_cookie_button.click()

# The cookie to click on
cookie_to_click = driver.find_element(By.ID, "cookie")

# Access the upgrade store
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie_to_click.click()

    if time.time() > TIMEOUT:
        # Access individual store item upgrade
        all_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Get individual item price
        for price in all_items:
            element_text = price.text

            # Convert string price item into an integer
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}

        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cash/cookie count
        money_element = driver.find_element(By.ID, "money").text

        if "," in money_element:
            money_element = money_element.replace(",", "")

        cookie_count = int(money_element)

        # Check affordable upgrades
        affordable_upgrades = {}

        for item_cost in cookie_upgrades:
            if cookie_count > item_cost:
                affordable_upgrades[item_cost] = cookie_upgrades[item_cost]

        # Purchase affordable upgrade
        try:
            highest_affordable_upgrade = max(affordable_upgrades)
        except ValueError:
            pass
        else:
            to_purchase = affordable_upgrades[highest_affordable_upgrade]
            purchase_upgrade = driver.find_element(By.ID, to_purchase)
            purchase_upgrade.click()

        timeout = time.time() + 15

    if time.time() > FIVE_MINUTES:
        cookie_per_second = driver.find_element(By.ID, "cps").text
        print(f"Cookie per second: {cookie_per_second}")
        break

time.sleep(LONG_WAIT_TIME)
