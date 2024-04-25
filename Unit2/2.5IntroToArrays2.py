#FRIDGE CONTENT INVENTORY MAKER
#You have been put in charge of making a list of the contents of the refridgerator. 
#Being the comp sci nerd you have slowly become, you decide to make it way more complicated than just using a sheet of paper and a pen
#The code below is your solution to the problem.

#Unfortunately, your code became corrupted and parts of it are now missing
#Missing code is denoted with a "___". Fill in/correct the missing code and verify that it works appropriately


#Create an array called "fridgeContents"
fridgeContents = []

#Create an infinite loop so we don't need to keep restarting the program for each food
while True:
    #Create a temporary variable that stores the typed in food
    data_to_add_to_array = input("Add Food (type 'x' to end): ")

    #if the user does not type 'x', store the data in the array
    if data_to_add_to_array != "x":
        fridgeContents.append(data_to_add_to_array)
    #And, if they do type 'x', break out of the infinite loop
    else:
        print("finished adding contents to array")
        break

#After breaking out the loop above ask user if they want to view the list or delete the list
print("Would you like to view (y) or delete (n) data?")
print_choice = input("y/n")
while True:
    #if they select 'y'
    if print_choice == "y":
        #print the contents of the array
        print(fridgeContents)
        #break out of the loop
        break
    #if they select 'n'
    elif print_choice == "n":
        print("deleting contents of array!")
        #clear the list
        fridgeContents.clear()
        #break from the loop
        break
    else:
        print("invalid selection, try again")
