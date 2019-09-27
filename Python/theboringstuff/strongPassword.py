#! python3
# strongPassword.py - Ensures that the password string passed is strong.
# Password must be:
# - at least 8 characters long
# - contain both uppercase and lowercase characters
# - have at least one digit

import re, getpass

# Password Regex
passRegex = re.compile(r'[a-z+')

myPass = getpass.getpass()

