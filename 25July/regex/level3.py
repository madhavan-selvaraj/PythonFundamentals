import re

text = "apple Mango DOG cat Zebra"

# Extract words starting with a capital letter.
capital_words = re.findall(r"\b[A-Z][a-zA-Z]*", text)

# Extract words starting with lowercase letters.
lower_case_words = re.findall(r"\b[a-z][a-zA-Z]*", text)

# Extract words containing only uppercase letters.
only_uppercase = re.findall(r"\b[A-Z][A-Z]+", text)

# Extract words ending with "e".
end_with_e = re.findall(r"\b[A-Za-z]*e\b", text)

# Extract every letter from A to F.
from_A_To_F = re.findall(r"[A-F]", text)


print(f"CAPITAL WORDS :{capital_words}")
print(f"lowercase words:{lower_case_words}")
print(f"Only upper case words:{only_uppercase}")
print(f'Words ending with "e":{end_with_e}')
print(f'Every letter from "A" to "F":{from_A_To_F}')
