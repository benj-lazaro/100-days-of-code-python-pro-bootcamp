import datetime as dt
import random
import smtplib

# Constant Variable(s)
QUOTES_FILE = "quotes.txt"
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "blank.slate.acct"
SENDER_EMAIL_PASSWORD = "password12345"
RECIPIENT_EMAIL = "test.dummy@yahoo.com"
DAY_TO_SEND = 0     # 0 = Monday, 6 = Sunday

# Global Variable(s)
email_message = ""
quote_list = []


def read_quote_file():
    """Open file, read the content & save to a list"""
    with open(QUOTES_FILE) as file:
        quotes = file.readlines()

    # Read content, strip the \n character at the end of each line & save to a list
    for quote in quotes:
        stripped_quote = quote.strip()
        quote_list.append(stripped_quote)


def send_inspirational_msg():
    """Send Inspiration Message via SMTP"""
    with smtplib.SMTP(SMTP_SERVER) as connection:
        # Establish a TLS connection
        connection.starttls()
        # Login using user credentials
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
        # Send email to intended recipient
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=email_message
        )


# Determine the current day of the week
now = dt.datetime.now()
today = now.weekday()

# Check if today is the day to send an inspirational message
if today == DAY_TO_SEND:
    # Open the file containing quotes
    read_quote_file()
    # Pick a random quote from the list
    quote_of_the_day = random.choice(quote_list)
    # Construct email subject title & append the inspirational message for the day
    email_message = f"Subject: Monday Motivation... \n\n{quote_of_the_day}"
    # Send inspirational message
    send_inspirational_msg()
