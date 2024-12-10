Weight=int(input("Enter your weight : "))
height=float(input("Enter your height : "))

BMI=round(Weight/height**2)

if BMI < 18.5:
    print(f"your BMI is {BMI} you are Underweight ")

elif BMI < 25:
    print(f"your BMI is {BMI} you are in normal range")

elif BMI < 30:
    print(f"your BMI is {BMI} you are in Overweight (Pre-obese)")

elif BMI < 35:
    print(f"Your BMI is {BMI} you are overweight Obese")

else :
    print(f"Your BMI is {BMI} your clinically Obese")


