# Pizza Delivery

print("Welcome to Python Pizza Deliveries\n")
print("Please enter you options or choices in single letter!")

print("Small Pizza: $15")
print("Medium Pizza: $20")
print("Large Pizza: $25")

print("Pepperoni for Small Pizza: +2")

print("Pepperoni for Medium or Large Pizza: +$3")

print("Extra cheese for any size pizza: +$1")

mdLg_pepperoni = 3
cheese = 1

size = input("What size pizza do you want? S, M, L ")

if size == "S":
    small = 15
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        sm = small + 2
    # elif add_pepperoni == "N":
    #     np = small
    extra_chess = input("Do you want extra chess? Y or N ")
    if extra_chess == "Y" and add_pepperoni == "Y":
        sc = sm + cheese
        print(f"You final bill is: ${sc}")
    elif add_pepperoni == "N" and extra_chess == "Y":
        pc = small + cheese
        print(f"Your final bill is: ${pc}")
    elif add_pepperoni == "Y" and extra_chess == "N":
        # pepNoChess = small + sm
        print(f"You final bill is: ${sm}")
    else:
        print(f"Your final bill is: ${small}")

if size == "M":
    medium = 20
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        mp = medium + mdLg_pepperoni
    extra_chess = input("Do you want extra chess? Y or N ")
    if extra_chess == "Y" and add_pepperoni == "Y":
        chpep = mp + cheese
        print(f"Your final bill is: ${chpep}")
    elif extra_chess == "N" and add_pepperoni == "Y":
        print(f"Your total bill is: ${mp}")
    elif extra_chess == "Y" and add_pepperoni == "N":
        mdch = medium + cheese
        print(f"Your final bill is: ${mdch}")
    else:
        print(f"You final bill is: ${medium}")

if size == "L":
    large = 25
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y":
        lg = large + mdLg_pepperoni
    extra_chess = input("Do you want extra chess? Y or N ")
    if extra_chess == "Y" and add_pepperoni == "Y":
        lgchpep = lg + cheese
        print(f"You final bill is: ${lgchpep}")
    elif extra_chess == "N" and add_pepperoni == "Y":
        print(f"Your final bill is: ${lg}")
    elif extra_chess == "Y" and add_pepperoni == "N":
        lgchess = large + cheese
        print(f"You final bill is: ${lgchess}")
    else:
        print(f"Your final bill is: ${large}")

