#1st National Bank of Browntown Online Banking Application

#has code loop over and over to check deposits, withdraws, and current balance
activeaccount = False

#Class Customer stores all objects with it 
class Customer(): 
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck 

    #This is the object to show your current balance
    def __init__(self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)

    #This is the object to hsow your current balance
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
    #This is the object to let you deposit money to account
    def deposit(self,amount):
    #Add the ability to deposit
        self.balance = self.balance + amount
        return self.balance 
    

    #Add the ability to check balance

#Start up screen
print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()

#Input name here 
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)

#While lets options loop on endlessly
while activeaccount == False:

    #User options to choose from
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance")
    choice = input("->")

    ##Choice 1 withdrawing 
    if choice == "1":
        try:
            print("How much are you withdrawing")
            amount = float(input("-> $ "))

            #Number amount for withdrawing 
            if amount < customer.balance:
    
                print("You have withdrawn $" , amount)

                print("Your balance is $" , customer.withdraw(amount))

            #If not sufficient number will not accept
            else:
                print("Error has occured only type numbers that your account has")
        except:
                print("Error has occured only type numbers that your account has")
    

        
    #Add a line that tells them their balance...after you have implemented balance check above


        #Choice 2 how much you want to deposit  
    if choice == "2":
        try:
            print("How much are you depositing")
            amount = float(input("-> $ "))
   
            #Option to enter how much you want to deposit if 0 or lower will not deposit
            if amount > int(0):
                print("You have deposited $" , amount)

                print("Your balance is $" , customer.deposit(amount))
            #if not a number or 0 or less will not accept 
            else:
                print("An error has occured only type numbers that are not 0 or negative")
        except:
                print("An error has occured only type numbers that are not 0 or negative")
            
    #Choice 3 show the user there balance
    if choice == "3":
    
        print("Your current balance is $" , float(customer.balance))
