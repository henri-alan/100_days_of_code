print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M our L? ")
pepperoni = input("Do you want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Select a valid size")

if pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Please pay ${bill}")

