print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
amount_per_person = bill_with_tip / people
print(f"Each person should pay ${round(amount_per_person, 2)}")
