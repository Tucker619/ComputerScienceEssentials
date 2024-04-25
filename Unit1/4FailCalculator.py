print("Welcome to the Grading Calculator")
print("This calculator grades your grade and sees if you passed or failed")
Num1 = int(input("Insert the points the grade was out of -> "))
Num2 = int(input("Insert the points the grade you scored -> "))
answer = ((Num2 / Num1) * int(100))
#per = ("%")
print(str(answer),"%") 
if answer >= int(60):
    print("You Pass")
else:
    print("You Fail")
