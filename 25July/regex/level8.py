import re

text = """
Alice scored 90
Bob scored 88
Charlie scored 95
"""

# Extract all names.
names = re.findall(r"[A-Z][a-z]+", text)

# Extract all marks.
marks = re.findall(r"\d{2}", text)

# Extract all words longer than five letters.
word_5 = re.findall(r"[A-Za-z]{6,}", text)

# Extract every word starting with A.
word_A = re.findall(r"\bA[a-zA-Z]+", text)

# Extract every word ending with "ed".
word_ed = re.findall(r"\b[A-Za-z]+ed\b", text)

print(f"Names:{names}")
print(f"Marks:{marks}")
print(f"All words longer than five letters:{word_5}")
print(f'Every word starting with "A":{word_A}')
print(f'Every word ending with "ed":{word_ed}')
