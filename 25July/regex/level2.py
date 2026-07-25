import re

text = "John123 lives in Chennai 600001."

# Extract all digits.
digits = re.findall(r"\d+", text)

# Extract all words.
words = re.findall(r"\w+", text)

# Extract all whitespace characters.
whitespace = re.findall(r"\s+", text)

# Extract every character except digits.
characters = re.findall(r"\D+", text)

# Find every occurrence of exactly one character followed by "ohn".
occurrences = re.findall(r".ohn", text)

# Extract every uppercase letter.
uppercase = re.findall(r"[A-Z]+", text)

# Extract every lowercase letter.
lowercase = re.findall(r"[a-z]+", text)

# Extract every vowel.
vowels = re.findall(r"[aeiou]+", text)

# Extract every character that is not a vowel.
consonants = re.findall(r"[^aeiou]+", text)


# print(f"Digits: {digits}")
# print(f"Words : {words}")
# print(f"Whitespace: {whitespace}")
# print(f"Characters: {characters}")
# print(f"Occurrences: {occurrences}")
# print(f"Uppercase: {uppercase}")
# print(f"Lowercase: {lowercase}")
# print(f"Vowels: {vowels}")
# print(f"Consonants: {consonants}")
