# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Diego Mejia>,<10/31/24>, <Created Script>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
--- Course Registration Program ---
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
-----------------------------------
"""
FILE_NAME: str = "Enrollments34.csv"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file_obj = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

#Read From File
'''
This For Loop is what allows us to save the input() data 
to the "Enrollements.csv" without trunkating the previous data
'''
try:
    file_obj = open(FILE_NAME, 'r') #By opening it up in "READ" mode, we don't overwrite the existing data
    for each_row in file_obj.readlines(): #Reads each line in the list[]
        student_data = each_row.split(',') #The split() removes the \n in line 71
        student_data = {"FirstName":student_data[0], "LastName":student_data[1], "CourseName":student_data[2].strip()} #Place holder of the structure of my dict{}
        #students.append(student_data) #Adds a list[] to the end of my list[]
    file_obj.close() #Basically saves my file
except FileNotFoundError as e:
    print(f'There is no file {FILE_NAME}')
    print(e,e.__doc__)
    file_obj = open(FILE_NAME,'w')
except Exception as e:
    print("There was an error opening the file")
    print(e,e.__doc__)    
finally:
    print("Closing File")
    file_obj.close()


# Present and Process the data
while True: 
    # Present the menu of choices
    print(MENU)
    menu_choice = input('What would you like to do? ')
    
    # Input user data
    if menu_choice == '1':
        try:
            student_first_name = input("Enter Student's First Name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must contain only letters")
                
            student_last_name  = input("Enter Student's Last Name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must contain only letters")
                
            course_name = input("Enter Course Name: ")
            csv_data = f"{student_first_name},{student_last_name},{course_name}\n"
            student_data = {"FirstName":student_first_name, "LastName":student_last_name, "CourseName":course_name} #What does my dict{} consist of?
            students.append(student_data) #Adds a dict{} to the end of my list[] of dict{}
        except ValueError as e:
            print("First and Last name must only contain letters")
            print(e,e.__doc__)
        continue

  
   
    # Present the current data
    elif menu_choice == '2':
        print('Current CSV Data: Last student entered in session ')
        print(csv_data)
        print('Current List Table: Full Table of all students registered ') 
        print(students)
        continue 
        
  
    
    # Save the data to a file
    elif menu_choice == '3':
        try:
            file_obj = open(FILE_NAME, "w") 
            for student in students:
                file_obj.write(f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n')
                if "FirstName" not in students[0]:
                    raise KeyError("First name not in dict{}")
                elif "LastName" not in students[0]:
                    raise KeyError("Last name not in dict{}")
                elif "CourseName" not in students[0]:
                    raise KeyError("Course name not in dict{}")
                else:
                    print("All keys found in dict{}")
        except IOError as e:
            print(f'Error writing data into {FILE_NAME}')
            print(e,e.__doc__)
        finally:
            print("Closing file")
            file_obj.close()
            print(f'{student["FirstName"]} {student["LastName"]} has registered for {student["CourseName"]} in this last user session!')
        continue

    # Stop the loop
    elif menu_choice == '4':
        break  
    
    else:
        print("INVALID CHOICE: Please choose options 1, 2, or 3")

    
print("Program Ended")    