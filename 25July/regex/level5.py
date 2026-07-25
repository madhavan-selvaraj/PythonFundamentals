import re

text1 = "Python is awesome"
text2 = "123abc"
text3 = "abc123"

# Check whether "Python is awesome" starts with "Python".
print(bool(re.match(r"^Python", text1)))

# Check whether "123abc" starts with digits.
print(bool(re.match(r"^\d", text2)))

# Check whether "abc123" starts with digits.
print(bool(re.match(r"^\d", text3)))
