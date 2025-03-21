import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Za-z']+(?: [A-Z-a-z]+)*$"
name_regex = re.compile(name)

phone_number = r"^\+?[0-9]{1,3}?[-.) ]?\(?[0-9]{2,4}\)?[-. ]?[0-9]{3,4}[-. ]?[0-9]{4}$"
phone_regex = re.compile(phone_number)

email_address = r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)

# name = r"^[A-Z][a-z']*(?: [A-Z][a-z'-]*)*$"
# name_regex = re.compile(name)