import datetime as dt
import time

# Import smtplib for the actual sending function
import smtplib, ssl

def send_email(password, hw, ddl, date):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "cheeryprojecttesting@gmail.com"  # My testing email address
    receiver_email = "qiw131@ucsd.edu"  # My UCSD address
    password = password
    message = """\
    Subject: Homework Reminder

    You need to finish this homework before midnight."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def send_email_at(password, hw, ddl, date):
    # if for some reason this script is still running
    # after a year, we'll stop after 365 days
    for i in range(0,365):
        future = dt.datetime(t.year,t.month,t.day,9,30)
        if t.hour >= 2:
            future += dt.timedelta(days=1)
        time.sleep((future-t).seconds)

        send_email(password, hw=hw, ddl=ddl, date=date)
        print("email sent")

t = dt.datetime.today()
while True:
    hw = input("""\
        What homework do you have? 
        (Enter Done if you don't have any homework to enter)""")
    if hw == "Done":
        break
    
    ddl = input("When is the deadline for this homework? (hr mm dd)")
    ddl_h = int(ddl[0:2])
    ddl_m = int(ddl[3:5])
    ddl_d = int(ddl[6:8])
    ddl_dt = t
    try:
        if ddl_m < t.month:
            t.year += 1 # handling due dates that are on the next year
        ddl_dt = dt.datetime(t.year, ddl_m, ddl_d, ddl_h)
    except TypeError:
        print("Please enter integers as hour, month, day")
    except ValueError:
        print("Please enter valid values for hour(0-23), month(1-12), day(1-31)")
    
    date = input("""\
        When do you want to be reminded of doing this homework? (hr mm dd)""")
    date_h = int(ddl[0:2])
    date_m = int(ddl[3:5])
    date_d = int(ddl[6:8])
    date_dt = t
    try:
        if date_m < t.month:
            t.year += 1 # handling due dates that are on the next year
        date_dt = dt.datetime(t.year, date_m, date_d, date_h)
    except TypeError:
        print("Please enter integers as hour, month, day")
    except ValueError:
        print("Please enter valid values for hour(0-23), month(1-12), day(1-31)")


password = input("Type your password and press enter: ")
send_email_at(password, hw, ddl_dt, date_dt)