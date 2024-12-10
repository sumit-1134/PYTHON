height=int(input("what is your height in feet : "))

if height>=3:
    print("You can ride")
    age=int(input("Enter your age : "))
    if age<=12:
        print("Pay  $ 250 ")

    elif age<=18:
        print("Pay $ 500")
    else:
        print("Pay $1000")


else:
    print("You cannot ride ")
    print("Bye bye........!")