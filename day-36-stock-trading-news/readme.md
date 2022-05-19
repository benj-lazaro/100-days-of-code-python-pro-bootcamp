## Stock Trading News app 
* Stack Trading News

### What does it do?
The Stock Trading News app will:
* Check the stocks of a targeted company (e.g. Tesla, Inc.) using AlphaVantage API (https://newsapi.org)
* Retrieve the closing stock price of yesterday & the day before
* Compose an SMS message is the percentage difference of the closing stock price > 5%
* Retrieve three (3) relevant news articles using NewsAPI (https://newsapi.org)
* Forwards the SMS message using Twilio API (https://www.twilio.com/)

### How does it work?
On the command-line (or terminal), type the following:<br>
* python3 <b>stock_trading_news.py</b>

<b>NOTE:</b> It is assumed that the <b>Python 3 interpreter</b> had already been installed on your computer.
