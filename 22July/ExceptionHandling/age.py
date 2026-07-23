class InvalidAgeError(Exception):
    pass


age = int(input("Enter you age:"))
try:
    if age < 18:
        raise InvalidAgeError("Age must be above 18")
    else:
        print("You are eligible")
except InvalidAgeError as e:
    print("Error:", e)
