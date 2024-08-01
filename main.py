print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = float(0)

if size == 'S':
    bill = float(15)
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
    print(f"Your total bill is ${bill}")
elif size == 'M':
    bill = float(20)
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"Your total bill is ${bill}")

elif size == 'L':
    bill = float(25)
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
    print(f"Your final bill is ${bill}")

else:
    print("Your isn't available ")