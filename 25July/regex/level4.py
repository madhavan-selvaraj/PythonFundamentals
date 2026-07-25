import re

text = "a aa aaa aaaa aaaaa"
text2 = "123 12345 987654 45678"

# Match one or more "a".
one_or_more = re.findall(r"\b[a]+\b", text)

# Match zero or more "a"
zero_or_more = re.findall(r"\b[a]*\b", text)

# Match exactly three "a".
exactly_three = re.findall(r"\ba{3}\b", text)

# Match between two and four "a".
two_or_more = re.findall(r"\ba{2,4}\b", text)

# Match atleast four "a"
atleast_four = re.findall(r"\ba{4,}\b", text)

# Extract all numbers having exactly 5 digits.
exact_5 = re.findall(r"\b\d{5}\b", text2)


print(f'Match one or more "a".{one_or_more}')
print(f'Match zero or more "a".{zero_or_more}')
print(f'Match exactly three "a".{exactly_three}')
print(f'Match between two and four "a".{two_or_more}')
print(f'Match at least four "a".{atleast_four}')
print(f"Extract all numbers having exactly 5 digits.{exact_5}")
