Balance_amount = 1000
print(f"You have Rs.{Balance_amount} in your account")
withdraw_amount = int(input("Enter withdraw amount:"))


if withdraw_amount < Balance_amount:
    print(f"Rs.{withdraw_amount} is Withdrawed")
if withdraw_amount > Balance_amount:
    raise ValueError("Withdraw Amount should be less than Balance Amount")
