import re

text1 = "Python 3.13 was released in 2024."

text2 = "Contact us at support@example.com"

text3 = "Alice scored 95 marks and Bob scored 88 marks."

new1 = re.match(r"Python", text1)

new2 = re.search(r"[\w.-]+@[\w.-]+\.\w+", text2)

new3 = re.search(r"(\w+)\s+(\d+)\s+(\w+)", text3)


print(f"matched text:{new1.group()}")
print(f"start position:{new1.start()}")
print(f"end position:{new1.end()}")
print(f"span:{new1.span()}")

print(new2.group())
print(len(new2.group()))

print(new3.group(1))
print(new3.group(3))
