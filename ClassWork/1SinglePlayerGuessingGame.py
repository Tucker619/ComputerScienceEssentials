#Single Player Guessing Game
#This Game allows a single user to guess a computer-generated number

#IMPORTS
import random

#VARIABLES
answer = -1
user_guess = -1
lives_counter = 10

#BEGIN GAME HERE
print("Welcome to the single player guessing game.")
print("Guess a number between 1-100")

answer = random.randint(1,100)
#print(answer)

#GAME LOOP
while(lives_counter > 0):
    print("What is your guess?")
    user_guess = int(input("->"))
    lives_counter -= 1
    print("your guess:", user_guess)
    print("You have", lives_counter, "lives left.")

    if user_guess == answer: 
        print("You Win")
        break
    elif user_guess > answer:
        print("Guess Lower")
    elif user_guess < answer:
        print("Guess Higher")
    else:
        print("An error has occured")
print("Thanks for playing!")
if lives_counter <=0:
    print("The secret number was", answer)
