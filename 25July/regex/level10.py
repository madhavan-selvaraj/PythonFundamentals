import re

text1 = "John123 lives at House 45, Chennai 600001. Call 9876543210."

text2 = "Python     is    a      powerful   programming      language."

text3 = """
Contact us at support@gmail.com.
Sales: sales@company.co.in
Personal: john.doe123@yahoo.com
"""

text4 = """
John: 9876543210
Alice: 9123456789
Office: 8012345678
Emergency: 9999999999
"""

# Replace every digit with "X".
new_text1 = re.sub(r"\d", "X", text1)

# Replace multiple spaces with one space.
new_text2 = re.sub(r"\s+", " ", text2)

# Replace every email with "EMAIL".
new_text3 = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "EMAIL", text3)

# Replace every phone number with "HIDDEN".
new_text4 = re.sub(r"\d+", "HIDDEN", text4)

print('\nevery digit with "X"\n')
print(f"Before:{text1}")
print(f"After:{new_text1}")

print("\nMultiple spaces with one space\n")
print(f"Before:{text2}")
print(f"After:{new_text2}")

print('\nEvery email with "EMAIL"\n')
print(f"Before:{text3}")
print(f"After:{new_text3}")

print('\nEvery phone number with "HIDDEN"\n')
print(f"Before:{text4}")
print(f"After:{new_text4}")
