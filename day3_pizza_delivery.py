print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill = 0


if size == "S":
    bill = 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 2
    else:
        bill = bill

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1
    else:
        bill = bill
    print(f"Your pizza cost: {bill}")


elif size == "M":
    bill = 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3

    else:
        bill = bill

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1

    else:
        bill = bill

    print(f"Your pizza cost: {bill}")

elif size == "L":
    bill = 25

    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3
    else:
        bill = bill

    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1
    else:
        bill = bill
    print(f"Your pizza cost: {bill}")

else:
    print("You tiped a invalid input")