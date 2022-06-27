from selenium import webdriver

# Constant Variable(s)
CHROME_DRIVER_PATH = "../chromedriver"

# Instantiate a Chrome webdriver object
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.amazon.com")
