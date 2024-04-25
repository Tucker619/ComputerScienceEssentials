#HOMEROOM ROSTER
#This program will keep track of students 
#It will perform the following tasks 1) how many kids are in homeroom 2) who is in homeroom 3) absences 

#Create Object called Student 
class Student:
    def __init__(self , name , locker_number , id , grade , age , address):
        self.name = name
        self.locker_number = locker_number
        self.id = id
        self.grade = grade
        self.age = age
        self.address = address

#Create the student list array:
list_of_homeroom_students = []

#Functions
def addToHomeroom():
    #Creates a student. Adds the mto the roster
    #Has Properties: name, locker number, id, grade, age, address

    #Name
    print("What is the student's name")
    name = input("->")

    #locker Number
    print("What is their assigned locker number:")
    locker_number = input("->")

    #id
    print("What is the student's ID number:")
    id = input("->")

    #grade
    print("What is the student's grade:")
    grade = input("->")

    #Age
    print("What is the student's age:")
    age = input("->")

    #Address
    print("What is the student's address")
    address = input("->")

    new_student = Student(name , locker_number , id , grade , age , address)
    print("New Student created with this information")
    print("name:", new_student.name)
    print("locker number:" , new_student.locker_number)
    print("ID number:" , new_student.id)
    print("Grade:" , new_student.grade)
    print("Age:" , new_student.age)
    print("Address:" , address)
    list_of_homeroom_students.append(new_student)

def getNumberOfStudentsInHomeroom():
    number_of_students = len(list_of_homeroom_students)
    return number_of_students
def searchForStudentInHomeroom(name):
    #Searches the roster  for a student. Says yes if student is on list
    for student in list_of_homeroom_students:
        if student.name == name:
            print("Student is on the list")
        return
    print("Student is not on the list")

def searchStudentAddress(name):
    for student in list_of_homeroom_students:
        if student.name == name:
            print(student.address)
    
def getListOfStudents():
    print("getting the list of students for you")
    for student in list_of_homeroom_students:
        print(student.name)
def getStudentID(name):
    for student in list_of_homeroom_students:
        if student.name == name:
            print(student.id)

def removeStudentFromList(name):
    for student in list_of_homeroom_students:
            if student.name == name:
                list_of_homeroom_students.remove(student)
                print("Removed Student")

#MAIN CODE 
while True:
    print("What would you like to do:")
    print("1: View homeroom roster")
    print("2: Add student to homeroom")
    print("3: Remove student from homeroom")
    print("4: Get a student's ID number")
    print("5: get number of students in homeroom")
    print("6: Search for student on list")
    print("7: Exit program")
    
    choice = int(input("->"))

    if choice == 1:
       #View Homeroom Roster print(getListOfStudents)
        getListOfStudents()
    elif choice == 2:
        #Add student to homeroom (create a new student)
        addToHomeroom()
    elif choice == 3:
        #Remove a student from the roster
        print("Which Student do you want to remove?")
        name = input("->")
        removeStudentFromList(name)
        
    elif choice == 4:
        #Print ID for a certain student in homeroom
        print("Which Student Do You Need and ID for?")
        choice = input("->")
        getStudentID(choice)

    elif choice == 5:
        #Print length of list (# of students)
        print(getNumberOfStudentsInHomeroom() , "students in homeroom")
    elif choice == 6:
        #search the list for a provided student name
        #prints the results ot the terminal
        print("What student do you want to search for?")
        name = input("->")
        searchForStudentInHomeroom(name)
    elif choice == 7:
        #Quit the program
        break
    else:
        #Give an error that they chose an incorrect menu option
        print("Selection Error has occured, try again")

#End of code
print("thanks for using the software")
