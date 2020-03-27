# Core modules

# import entire module
import datetime
import re

# import a part of a module
from datetime import date

# import time function from time module
from time import time

# Pip module
from camelcase import CamelCase

# In JS
# node modules


# today = datetime.date.today()
today = date.today()

# timestamp = time.time()
timestamp = time()

c = CamelCase()
print(c.hump("hello there world"))


def validate_email(email):
    if len(email) > 7:
        return bool(
            re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email)
        )


email = "test#test.com"
if validate_email(email):
    print("Email is valid")
else:
    print("Email is bad")
