print("Welcome to the Grading Calculator")
print("This calculator grades your grade and sees what grade you got an A, B, C, D, or F")
Num1 = int(input("Insert the points the grade was out of -> "))
Num2 = int(input("Insert the points the grade you scored -> "))
answer = ((Num2 / Num1) * int(100))
print(str(answer),"%") 
if answer >= int(90):
    print("You got an A")
elif answer >= int(80):
    print("You got a B")
elif answer >= int(70):
    print("You got a C")
elif answer >= int(60):
    print("You got a D")
else:
    print("You got a F do better")
