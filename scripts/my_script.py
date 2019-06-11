"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
import datetime as dt
from my_module.functions import send_email, send_email_at

###
###

t = dt.datetime.today()
while True:
    hw = input("What homework do you have? (Enter Done if you don't have any homework to enter)")
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
        print("Please enter valid values for hour(00-23), month(01-12), day(01-31)")
    
    date = input("When do you want to be reminded of doing this homework? (hr mm dd)")
    date_h = int(ddl[0:2])
    date_m = int(ddl[3:5])
    date_d = int(ddl[6:8])
    date_dt = t
    try:
        if date_m < t.month:
            t.year += 1 # handling reminder dates that are on the next year
        date_dt = dt.datetime(t.year, date_m, date_d, date_h)
    except TypeError:
        print("Please enter integers as hour, month, day")
    except ValueError:
        print("Please enter valid values for hour(00-23), month(01-12), day(01-31)")


password = input("Type your password and press enter: ")
send_email_at(password, hw, ddl_dt, date_dt)
