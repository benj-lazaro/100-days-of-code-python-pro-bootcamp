from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instantiate a Chrome object and install the corresponding webdriver version
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Launch Chrome and retrieve the targeted web page
driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")

# Retrieve the item's price from the targeted web page using CSS selector
price = driver.find_element(By.CSS_SELECTOR, "span.a-price.a-text-price.a-size-medium.apexPriceToPay")
print(price.text)

# Terminate the current Chrome browser
driver.quit()
