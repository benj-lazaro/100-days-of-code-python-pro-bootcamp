from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Instantiate a Chrome object and install the corresponding webdriver version
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Launch Chrome and retrieve the targeted web page
driver.get("https://www.python.org/")

# Search element by its HTML attribute name
search_bar = driver.find_element(By.NAME, "q")

# Retrieve & print the targeted element's associated tag name
print(f"HTML tag: {search_bar.tag_name}")

# Retrieve & print the targeted element's associated HTML attribute
print(f"HTML attribute placeholder: {search_bar.get_attribute('placeholder')}")

# Search element by its HTML attribute class
logo = driver.find_element(By.CLASS_NAME, "python-logo")

# Retrieve & print the element's size and associated HTML attribute src
print(f"Image size: {logo.size}")
print(f"Image filename & path: {logo.get_attribute('src')}")

# Search element using CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(f"Documentation URL: {documentation_link.text}")

# Search element using XPath (use Dev Tools to retrieve the associated XPath)
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f"Link text: {bug_link.text}")


# Terminate the current Chrome browser
driver.quit()
