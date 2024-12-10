Height=int(input("Enter your Height in feet : "))
Bill=0
if Height>=3:
    print("You can ride")

    age=int(input("Enter your age :"))
    if age<12:
        Bill=120
        print("Pay $120")
    elif age<=18:
        Bill=250
        print("Pay $250")
    else :
        Bill=500
        print("print $500")

    Photos=input("If you want photos (Y/N) : ")
    if Photos == 'y' or Photos == 'Y':
        PH=  Bill +50
        print(f"Your total bill is {PH} ")
        print("Thank you. Enjoy the ride !!")

    else:
        print(f"Your total bill is {Bill}")
        print("Thank you. Enjoy the ride !!")




else:
    print("you can't ride")
    