import re

phone_numbers = [
    "9876543210",  # Valid
    "123456789",  # Invalid (9 digits)
    "98765432101",  # Invalid (11 digits)
    "98765abcd0",  # Invalid (contains letters)
    "98765 43210",  # Invalid (space)
]

pins = [
    "123456",  # Valid
    "654321",  # Valid
    "12345",  # Invalid (5 digits)
    "1234567",  # Invalid (7 digits)
    "12a456",  # Invalid (contains letter)
]

usernames = [
    "john1",  # Valid
    "Alice_2025",  # Valid
    "a_bc12",  # Valid
    "1john",  # Invalid (starts with digit)
    "_john",  # Invalid (starts with _)
    "ab",  # Invalid (too short)
    "this_is_a_very_long_username",  # Invalid (too long)
    "john-doe",  # Invalid (- not allowed)
]

passwords = [
    "Password1",  # Valid
    "Hello123",  # Valid
    "python123",  # Invalid (no uppercase)
    "PYTHON123",  # Invalid (no lowercase)
    "Password",  # Invalid (no digit)
    "Pass1",  # Invalid (too short)
    "welcome9A",  # Valid
]

dates = [
    "2025-07-25",  # Valid
    "1999-12-31",  # Valid
    "2025-7-25",  # Invalid (month not 2 digits)
    "25-07-2025",  # Invalid
    "2025/07/25",  # Invalid
    "2025-13-99",  # Format valid (logical date invalid)
    "abcd-12-31",  # Invalid
]

# Validate a 10-digit phone number.
print("Phone number Validation:")
for number in phone_numbers:
    if re.fullmatch(r"\d{10}", number):
        print(f"{number}:Valid")
    else:
        print(f"{number}:Invalid")

# Validate a PIN containing exactly 6 digits.
print("\nPin number Validation:")
for pin in pins:
    if re.fullmatch(r"\d{6}", pin):
        print(f"{pin}:Valid")
    else:
        print(f"{pin}:Invalid")

# Validate a username:
# Starts with a letter
# Can contain letters, digits, _
# Length: 5–15 characters
print("\nUser name Validation:")
for name in usernames:
    if re.fullmatch(r"^[A-Za-z]\w{4,14}$", name):
        print(f"{name}:Valid")
    else:
        print(f"{name}:Invalid")

# Validate a password:
# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
print("\nPassword Validation:")
for password in passwords:
    if re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}", password):
        print(f"{password}:Valid")
    else:
        print(f"{password}:Invalid")

# Validate dates in the format:YYYY-MM-DD
print("\nDate Validation:")
for date in dates:
    if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", date):
        print(f"{date}:Valid")
    else:
        print(f"{date}:Invalid")
