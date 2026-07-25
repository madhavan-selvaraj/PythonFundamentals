import re

text1 = "Age 20 Roll 101"

text2 = """
Contact us at support@example.com for help.
You can also email admin123@company.org or test.user@gmail.com.
"""

text3 = "I was walking while singing and laughing before starting the race."

# Find the first number
number = re.search(r"\d+", text1)

# Find the first uppercase word.
word = re.search(r"[A-Z][a-zA-Z]+", text1)

# Find the first email address.
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text2)

# Find the first word ending in "ing".
ing_word = re.search(r"\b[A-Za-z]+ing\b", text3)

print(f"The first number:{number.group()}")
print(f"The first uppercase word:{word.group()}")
print(f"The first email address:{email.group()}")
print(f'The first word ending in "ing":{ing_word.group()}')
