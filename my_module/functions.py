"""A collection of function for doing my project."""

import time

# Import smtplib for the actual sending function
import smtplib
import ssl

import datetime as dt


def send_email(password, sender, receiver, hw):
    """ Send one homework email reminder. This function is mostly an adaptation
    from code on this website: https://realpython.com/python-send-email/#getting-started.
    The only part I contributed is the message customization based on the homework
    parameter.
    
    Parameters
    ----------
    password : str
        The password to sender's email address. 
    sender : str
        Email reminder sender's email address.
    receiver : str
        Email reminder receiver's email address.
    hw : tuple
        A tuple whose elements are homework name (str), reminder date (dt.datetime), 
        and deadline (dt.datetime)
    
    Returns
    -------
    None 
    """

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = sender
    receiver_email = receiver
    ddl_str = hw[1].strftime("%Y-%m-%d %H:%M")
    message = """\
    Subject: Homework %s Reminder

    You need to finish %s before %s.""" % (hw[0], hw[0], ddl_str)

    context = ssl.create_default_context()

    # Email login and sending handler
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def remind_date(t):
    """ A helper function that gets reminder date from hw tuple in send_timed_email(). 
    
    Parameters
    ----------
    t : tuple
        hw variable passed in from send_timed_email. 
    
    Returns
    -------
    t[-1] : dt.datetime
        The date when the reminder needs to be sent. 
    """

    return t[-1]


def send_timed_email(password, sender, receiver, hws):
    """ Send reminder emails for every homework. I got email timing idea for this 
    function from this post: 
    https://stackoverflow.com/questions/2031111
    /in-python-how-can-i-put-a-thread-to-sleep-until-a-specific-time
    Line 102 and 103 are an adaptation of the code from this post. I also learned how to
    sort tuples by one value in it from this post:
    https://stackoverflow.com/questions/4554115/sorting-tuples-in-python-with-a-custom-key
    The use of sorted() and helper function remind_date() is an adaptation of the code
    from this post. 
    
    Parameters
    ----------
    password : str
        The password to sender's email address. 
    sender : str
        Email reminder sender's email address.
    receiver : str
        Email reminder receiver's email address.
    hws : list of tuples
        A list of tuple whose elements are homework name (str), reminder date 
        (dt.datetime), and deadline (dt.datetime)
    
    Returns
    -------
    None 
    """

    hws = sorted(hws, key=remind_date)

    #  Send email reminder for each homework at its specified time
    for hw in hws:
        t = dt.datetime.today()
        time.sleep((hw[-1] - t).seconds)

        send_email(password=password, sender=sender, receiver=receiver, hw=hw)
        print("email sent")

