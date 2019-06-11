"""A collection of function for doing my project."""

import datetime as dt
import time

# Import smtplib for the actual sending function
import smtplib, ssl

def send_email(password, hw, ddl):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "cheeryprojecttesting@gmail.com"  # My testing email address
    receiver_email = "qiw131@ucsd.edu"  # My UCSD email address
    #password = password
    ddl_str = ddl.strftime("%Y-%m-%d %H:%M")
    message = """\
    Subject: Homework %s Reminder

    You need to finish %s before %s.""" % (hw, hw, ddl_str)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def send_email_at(password, hw, ddl, date):
    # if for some reason this script is still running
    # after a year, we'll stop after 365 days
    for i in range(0,365):
        t = dt.datetime.today()
        time.sleep((date-t).seconds)

        send_email(password=password, hw=hw, ddl=ddl)
        print("email sent")

