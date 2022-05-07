import datetime as dt
import random
import smtplib

# Constant Variable(s)
QUOTES_FILE = "quotes.txt"
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "blank.slate.acct"
SENDER_EMAIL_PASSWORD = "password12345"
RECIPIENT_EMAIL = "test.dummy@yahoo.com"

# Global Variable(s)
email_message = ""
quote_list = []


def read_quote_file():
    """Open quotes file, pick one per line & save each entry to a list"""
    with open(QUOTES_FILE) as file:
        quotes = file.readlines()

    # Read each quote & strip the \n character at the end
    for quote in quotes:
        stripped_quote = quote.strip()
        quote_list.append(stripped_quote)


# Get the current day of the week
now = dt.datetime.now()
today = now.weekday()

# Check if today is Monday (0)
if today == 0:
    # Open quote file & pick a random quote
    read_quote_file()
    quote_of_the_day = random.choice(quote_list)
    # Construct email subject & message content
    email_message = f"Subject: Monday Motivation... \n\n{quote_of_the_day}"

    # Access email account & then send message
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=email_message
        )
