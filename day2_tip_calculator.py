print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


each_person_bill = float((bill / people) * (1 + tip / 100))
final_amount = round(each_person_bill, 2)

print(f"Each person should pay {final_amount}")
