import re

text = """
Alice scored 90
Bob scored 88
Charlie scored 95
"""

email = """
Contact us at support@gmail.com.
Sales: sales@yahoo.com
Personal: john.doe123@outlook.com
Backup: admin@test.org
"""

sentence = (
    "Python is a powerful programming language used for automation and web development."
)

# Print every number and its position.
print("Every number and its position")
numbers = re.finditer(r"\d+", text)
for number in numbers:
    print(f"{number.group()}-{number.span()}")


# Print every email and its start position.
print("\nEvery email and its start position")
emails = re.finditer(r"[\w.-]+@[\w.-]+\.\w+", email)
for i in emails:
    # pass
    print(f"{i.group()}-{i.start()}")


# Print every word and its length.
print("\nEvery word and its length")
words = re.finditer(r"[A-Za-z]+", sentence)
for word in words:
    print(f"{word.group()}-{len(word.group())}")
