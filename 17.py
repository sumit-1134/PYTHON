Name1=input("What is your name :")
Name2=input("What is his/her name :")

Combime_string=Name1 + Name2 
lower_case=Combime_string.lower()


t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')

true=t+r+u+e

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')

love=l+o+v+e

love_score=int (str(true)+str(love))


if love_score < 10 or love_score>90:
    print(f"Your score is{love_score} and you go together like coke and mentos")

elif love_score >=40 or love_score<=50:
    print(f"Your love score is {love_score} and you are alright together")

else :
    print(f"Yor love score is {love_score}")