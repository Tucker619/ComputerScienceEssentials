fileName = "test_File.txt"

def writeToFile(content):
    try: 
        with open(fileName, 'a') as file:
            content = "\n" + content
            file.write(content)
            print("Content added!")
            file.close()
    except:
        print("An Error Has Occured!")

def readFromFile():
    try: 
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An Error Has Occured!")

def deleteFromFile():
    try:
        with open(fileName, 'w') as file:
            file.write(" ")
            print("Data Has Been Deleted!")
    except:
        print("An Error Has Occured!")

while True:
    print("Select An Option")
    print("1) Sign In   2) Check Signed In   3) Delete Signed In Data   4) Exit Software")

    choice = input("-> ")
    if choice == "1": 
        print("Please Sign In")

        content = input("-> ")
        writeToFile(content)

    elif choice == "2":

        readFromFile()

    elif choice == "3":
       
        deleteFromFile()
    
    elif choice == "4":

        break
        
