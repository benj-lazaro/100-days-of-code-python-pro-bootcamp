import smtplib

# Constant Variable(s)
SMTP_SERVER = "smtp.gmail.com"
MY_EMAIL = "blank.slate.acct"
MY_EMAIL_PASSWORD = "password12345"
EMAIL_RECIPIENT = "test.dummy@yahoo.com"
EMAIL_MSG = "Subject: Test Message 000\n\n This is the body of my email."

# Set up a connection to the SMTP server
with smtplib.SMTP(SMTP_SERVER) as connection:
    # Start a TLS session
    connection.starttls()
    # Login to email account using credentials
    connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
    # Send test message to email recipient via email
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=EMAIL_RECIPIENT,
        msg=EMAIL_MSG
    )
