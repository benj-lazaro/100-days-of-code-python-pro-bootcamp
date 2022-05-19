import requests
import os
from twilio.rest import Client

# Constant Variable(s)
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ['NEWS_API_KEY']
NEWS_API_PARAMETERS = {
    "qInTitle": COMPANY_NAME,
    "language": "en",
    "apiKey": NEWS_API_KEY,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ['STOCK_API_KEY']
STOCK_API_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

# Get stock information using AlphaVantage API (https://www.alphavantage.co/documentation/#daily)
response = requests.get(STOCK_ENDPOINT, params=STOCK_API_PARAMETERS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
day_before_data = data_list[1]
day_before_closing_price = day_before_data["4. close"]

# Find the difference in the closing stock price between yesterday and the day before
difference = float(yesterday_closing_price) - float(day_before_closing_price)

# Display an Up or Down emoji based on the closing stock price difference
up_down = None
if difference > 0:
    up_down = "▲"
else:
    up_down = "▼"

# Get the percentage difference in price between closing price of yesterday & the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

# If the stock price increase by 5% between yesterday and the day before yesterday then send relevant news article(s)
if abs(diff_percent) > 5:
    # Access the NewsAPI (https://newsapi.org/)
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_API_PARAMETERS)
    news_response.raise_for_status()
    news_articles = news_response.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    # https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = news_articles[:3]

    # Create a new list of the first 3 articles; show headline & description using list comprehension
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\n" 
                          f"Headline: {article['title']}. \nDescription: "
                          f"{article['description']}" for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+15169089084",
            to="+123456789"
        )

        print(message.status)
