print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill?\n $"))
tip_percentage = float(input("How much tip would you like to give?\n $"))
people_split = int(input("How many people to split the bill?\n $"))

payment_each = round((total_bill * (tip_percentage / 100 + 1)) / people_split, 2)
print(f"Each person should pay: ${payment_each}")
