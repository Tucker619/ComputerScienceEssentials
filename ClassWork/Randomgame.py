print("Dice Roller")
print("Choose how many dice you want to roll one di, two dice, or three dice")
print("For one di type 1")
print("For two dice type 2")
print("For three dice type 3")
dice_number = input("Input number of dice here -> ")

import random

if dice_number == "1":
    print("You have chosen to roll one di")
    print("If you want 6 sided dice type 6")
    print("If you want 10 sided dice type 10")
    print("If you want 12 sided dice type 12")
    print("If you want 20 sided dice type 20")
    dice_number1 = input("Choose sided di number here -> ")
    if dice_number1 == "6":
        random_number1 = random.randint(1,6) 
    elif dice_number1 == "10":
        random_number1 = random.randint(1,10) 
    elif dice_number1 == "12":
        random_number1 = random.randint(1,12) 
    elif dice_number1 == "20":
        random_number1 = random.randint(1,20) 
    else: 
        print("Error please try again")
    print("Your dice roll is" , random_number1)
elif dice_number == "2":
    print("You have chosen to roll two dice")
    print("If you want 6 sided dice type 6")
    print("If you want 10 sided dice type 10")
    print("If you want 12 sided dice type 12")
    print("If you want 20 sided dice type 20")
    dice_number1 = input("Choose first sided di number here -> ")
    if dice_number1 == "6":
        random_number1 = random.randint(1,6) 
    elif dice_number1 == "10":
        random_number1 = random.randint(1,10) 
    elif dice_number1 == "12":
        random_number1 = random.randint(1,12) 
    elif dice_number1 == "20":
        random_number1 = random.randint(1,20) 
    else:
        print("Error please try again")
    print("If you want 6 sided dice type 6")
    print("If you want 10 sided dice type 10")
    print("If you want 12 sided dice type 12")
    print("If you want 20 sided dice type 20")
    dice_number2 = input("Choose second sided di number here -> ")
    if dice_number2 == "6":
        random_number2 = random.randint(1,6) 
    elif dice_number2 == "10":
        random_number2 = random.randint(1,10) 
    elif dice_number2 == "12":
        random_number2 = random.randint(1,12) 
    elif dice_number2 == "20":
        random_number2 = random.randint(1,20) 
    else:
        print("Error please try again")
    print("Your first dice roll is" , random_number1)
    print("Your second dice roll is" , random_number2)
elif dice_number == "3":
    print("You have chosen to roll three dice")
    print("If you want 6 sided dice type 6")
    print("If you want 10 sided dice type 10")
    print("If you want 12 sided dice type 12")
    print("If you want 20 sided dice type 20")
    dice_number1 = input("Choose first sided di number here -> ")
    if dice_number1 == "6":
        random_number1 = random.randint(1,6) 
    elif dice_number1 == "10":
        random_number1 = random.randint(1,10) 
    elif dice_number1 == "12":
        random_number1 = random.randint(1,12) 
    elif dice_number1 == "20":
        random_number1 = random.randint(1,20) 
    else:
        print("Error please try again")
    print("If you want 6 sided dice type 6")
    print("If you want 10 sided dice type 10")
    print("If you want 12 sided dice type 12")
    print("If you want 20 sided dice type 20")
    dice_number2 = input("Choose second sided di number here -> ")
    if dice_number2 == "6":
        random_number2 = random.randint(1,6) 
    elif dice_number2 == "10":
        random_number2 = random.randint(1,10) 
    elif dice_number2 == "12":
        random_number2 = random.randint(1,12) 
    elif dice_number2 == "20":
        random_number2 = random.randint(1,20) 
    else:
        print("Error please try again")
    print("If you want 6 sided dice type 6")
    print("If you want 10 sided dice type 10")
    print("If you want 12 sided dice type 12")
    print("If you want 20 sided dice type 20")
    dice_number3 = input("Choose third sided di number here -> ")
    if dice_number3 == "6":
        random_number3 = random.randint(1,6) 
    elif dice_number3 == "10":
        random_number3 = random.randint(1,10) 
    elif dice_number3 == "12":
        random_number3 = random.randint(1,12) 
    elif dice_number3 == "20":
        random_number3 = random.randint(1,20) 
    else:
        print("Error please try again")
    print("Your first dice roll is" , random_number1)
    print("Your second dice roll is" , random_number2)
    print("Your third dice roll is" , random_number3)


    
