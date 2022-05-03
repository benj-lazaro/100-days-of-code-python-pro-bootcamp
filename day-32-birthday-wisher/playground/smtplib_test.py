import smtplib

SMTP_SERVER = "smtp.gmail.com"
my_email = "sn.kuroshiro"
my_password = "heybroheybro"
recipient_email = "thomas.nunez@yahoo.com"

with smtplib.SMTP(SMTP_SERVER) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg="Subject: Test Message 000\n\n This is the body of my email."
    )
