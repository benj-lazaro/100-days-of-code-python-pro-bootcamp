import datetime as dt
import pandas
import random
import smtplib

# Constant Variable(s)
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "dummy.account"
SENDER_EMAIL_PASSWORD = "password12345"

# Check today's month and date
today = (dt.datetime.now().month, dt.datetime.now().day)

# Read the CSV file
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# Check if there is someone else's birthday today
if today in birthday_dict:
    # Get the recipient's name
    birthday_person = birthday_dict[today]
    # Select a random birthday letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # Open the chosen random letter template
    with open(file_path, "r") as letter:
        contents = letter.read()
        # Replace placeholder [NAME] with the recipient's name
        birthday_message = contents.replace("[NAME]", birthday_person["name"])

    # Send the birthday greeting via SMTP
    with smtplib.SMTP(SMTP_SERVER) as connection:
        # Establish a TLS connection
        connection.starttls()
        # Login using user credentials
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
        # Compose birthday email to intended recipient
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{birthday_message}"
        )
