size = input("Tell me the size of the pizza (S/M/L): ")
bill = 0

if size == 'S':
    bill = 100
elif size == 'M':
    bill = 200
elif size == 'L':
    bill = 300
else:
    print("Invalid size selected.")
    exit()

pepperoni = input("Do you want Pepperoni? (Y/N): ")
if pepperoni == 'Y':
    if size == 'S':
        bill += 30
    else:
        bill += 50

cheese = input("Do you want extra Cheese? (Y/N): ")
if cheese == 'Y':
    bill += 20

print(f"Your total bill is {bill}")
