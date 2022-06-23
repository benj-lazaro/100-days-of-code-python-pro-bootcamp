from bs4 import BeautifulSoup
import requests
import smtplib
import os

# Constant Variable(s)
SENDER_EMAIL = os.environ.get("EMAIL_ACCOUNT")
SENDER_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT_NUMBER = 587
RECIPIENT_EMAIL = os.environ.get("TARGET_EMAIL_ADDRESS")

# Global Variable(s)
amazon_item_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
target_purchase_price = 100.00
# Client browser header information c/o http://myhttpheader.com/
client_browser_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36 "
}

# Request for a copy of the targeted Amazon item's web page
response = requests.get(amazon_item_url, headers=client_browser_headers)
html_file = response.text

# Scrape the web page for the item's current price
soup = BeautifulSoup(html_file, 'lxml')
amazon_item_name = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()\
    .strip()
amazon_current_price = soup.find(name="span", class_="a-offscreen").getText()
amazon_price = float(amazon_current_price.split('$')[1])

# If current price meets the targeted purchase price, send an email alert
if amazon_price <= target_purchase_price:
    print("Sending an email alert.")

    message_body = f"This item is currently within your ${str(target_purchase_price).split('.')[0]} budget! " \
                   f"So, what are you waiting for? \nClick the link {amazon_item_url} to purchase. Hurry!"

    message = f"Price Alert! {amazon_item_name}\n\n{message_body}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT_NUMBER) as connection:
        connection.starttls()
        result = connection.login(SENDER_EMAIL, SENDER_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=RECIPIENT_EMAIL,
                            msg=f"{message}")
else:
    print("Nope, not today. Will check the item again tomorrow.")
