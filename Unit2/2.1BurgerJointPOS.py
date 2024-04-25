#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheeseburger $6.00")
        print("3: Western Burger (Cheese, onion, western sauce) $6.75")
        print("4: Extra Burger (Extra beef, extra cheese, extra onions) $9.00")
        print()
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $" , totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $" , totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost + 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $" , totalCost)
        
        elif burgerChoice == "4":
        #BURGER 4: EXTRA BURGER
            totalCost = totalCost + 9.00
            print("You added Extra Burger to your order")
            print("Your total cost so far: $" , totalCost)


            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("We offer the following sides: ")
        print("1: Fries $3.25" )
        print("2: Kelp Fries (Potatoes in salt water) $5.00")
        print("3: Chum Stick (May cause vomitting) $6.50")
        print("4: The Side (No one knows what this is) $14.75")
        print()
        sideChoice = input("What would you like (input a number 1-4): ")
        #Add your Code/Comments Here for sides
        #Add at least three sides
        if sideChoice == "1":
            totalCost = totalCost + 3.25
            print("You added Fries to your order")
            print("Your total cost so far: $" , totalCost)

        #SIDE 2: KELP FRIES
        elif sideChoice == "2":
            totalCost = totalCost + 5.00
            print("You added Kelp Fries to your order")
            print("Your total cost so far: $" , totalCost)

        #SIDE 3: CHUM STICK
        elif sideChoice == "3":
            totalCost = totalCost + 6.50
            print("You added Chum Stick to your order")
            print("Your total cost so far: $" , totalCost)
        
        elif sideChoice == "4":
        #SIDE 4: THE SIDE
            totalCost = totalCost + 14.75
            print("You added The Side to your order")
            print("Your total cost so far: $" , totalCost)


        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Drinks":
        print("We offer the following drinks: ")
        print("1: Shake $2.25" )
        print("2: Ice Shake (Has ice) $3.25")
        print("3: Kelp Shake (NOT RESPONSIBLE FOR ANY KELP GROWING ON ONESELF) $5.25")
        print("4: The Drank (No one knows just tastes good) $7.75")
        print()
        
        drinkChoice = input("What would you like (input a number 1-4): ")
        #Add your Code/Comments Here for sides
        #Add at least three sides
        if drinkChoice == "1":
            totalCost = totalCost + 2.25
            print("You added Shake to your order")
            print("Your total cost so far: $" , totalCost)

        #DRINK 2: 
        elif drinkChoice == "2":
            totalCost = totalCost + 3.25
            print("You added Ice Shake to your order")
            print("Your total cost so far: $" , totalCost)

        #DRINK 3: 
        elif drinkChoice == "3":
            totalCost = totalCost + 5.25
            print("You added Kelp Shake to your order")
            print("Your total cost so far: $" , totalCost)
        
        elif drinkChoice == "4":
        #DIRNK 4: 
            totalCost = totalCost + 7.75
            print("You added The Drank to your order")
            print("Your total cost so far: $" , totalCost)


        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        #Add Your code/Comments here for Drinks
        #Add at least three drinks
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()
        if burgerChoice == "1":
            BurgerOrderVariable = "Hamburger"
        elif burgerChoice == "2":
            BurgerOrderVariable = "Cheeseburger"
        elif burgerChoice == "3":
            BurgerOrderVariable = "Western Burger"
        elif burgerChoice == "4":
            BurgerOrderVariable = "Extra Burger"
        else:
            BurgerOrderVariable = " "

        if sideChoice == "1":
            SideOrderVariable = "Fries"
        elif sideChoice == "2":
            SideOrderVariable = "Kelp Fries"
        elif sideChoice == "3":
            SideOrderVariable = "Chum Stick"
        elif sideChoice == "4":
            SideOrderVariable = "The Side"
        else:
            SideOrderVariable = " "
        
        if drinkChoice == "1":
            DrinkOrderVariable = "Shake"
        elif drinkChoice == "2":
            DrinkOrderVariable = "Ice Shake"
        elif drinkChoice == "3":
            DrinkOrderVariable = "Kelp Shake"
        elif drinkChoice == "4":
            DrinkOrderVariable = "The Drank"
        else:
            DrinkOrderVariable = " "
        

        #GIVE THEM THEIR TOTALS
        #Finish this section to give you a grand total as well as print your complete order
        print("Order finished")
        print("You have ordered")
        print(BurgerOrderVariable)
        print(SideOrderVariable)
        print(DrinkOrderVariable)
        print("Subtotal: $", totalCost)
        totalTax = round(float(totalCost) * tax , 2)
        print("Total Tax: $" , totalTax)
        print("Grand Total: $" , totalCost + totalTax)
        
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us" , name + "!")
