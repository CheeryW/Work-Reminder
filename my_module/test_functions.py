"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import datetime as dt
from functions import send_timed_email, remind_date

##
##

def test_remind_date():
    assert remind_date((9, 0)) == 0
