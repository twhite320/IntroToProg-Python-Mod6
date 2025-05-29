# --------------------------------------------------------------------------------------#
# Title: Assignment06
# Desc: This assignment demonstrates using functions, classes, and using separation of
# concerns
# Change Log: (Who, When, What)
# Tellrell White,05/28/2025,Created Script
# --------------------------------------------------------------------------------------#
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


#----------------Processing -------------------------------------------------------------#

class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    Changelog: (Who, When, What)
    Tellrell White, 05/28/30, Created Class

    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads JSON data and stores it into a list
               
        ChangeLog: (Who, When, What)
        Tellrell White,05/28/25,Created function

        #add params in
        :param file_name: storing name of file to read data from
        :param student_data: list of dictionary rows containing student data from JSON file

        :return: list  
        """

        file: None # Local variable
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script! \nIf file "
                                     "exists make sure it is closed!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name:str, student_data:list):
        """ This function writes a list of data to a JSON file 
               
        ChangeLog: (Who, When, What)
        Tellrell White,05/28/25,Created function

        #add params in
        :param file_name: storing name of file to write used for writing data
        :param student_data: list of dictionary rows containing student data from JSON file

        :return: none  
        """
        file: None  # Local variable
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        #Fix this error handling, message and message + and
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()


#----------------Presentation-------------------------------------------------------------------------#
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Tellrell White, 05/28/25, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        Tellrell White,05/28/25,Created function

        #add params in
        :param message: Custom error message
        :param error: Prints technical error message, documentation, and Error type

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu:str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Tellrell White,05/28/25,Created function

        param: menu: contains list of options for user

        :return: None
        """
        #Present the menu of choices
        print() # Adding space to make it look better
        print(menu)
        print() # Adding extra space to make it look better

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu selection from the user

        :return: string with the user's choice
        """
        choice = "0"
        choice = input("Enter your menu choice number: ")
        return choice

    @staticmethod
    def output_student_courses(student_data:list):
        """ This function displays the letter grades base on their GPA to the user

        ChangeLog: (Who, When, What)
        Tellrell White,05/28/25,Created function

        param: student_data: list of dictionary rows containing student data

        :return: None
        """
        #Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
            f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        print() #Added space for presentation

    @staticmethod
    def input_student_data(student_data:list):
        """
        This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        Tellrell White,05/28/25,Created function

        param: student_data: list of dictionary rows containing student data

        :return: list 
        """
        try:
            #Get input data from the user
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            registration_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(registration_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
           IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data
 

#------------------------------  End of Class definitions--------------------------------------------------#


# Beginning of the main body of this script

#Reading in data from JSON file and storing it in a variable                
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    #Prints menu
    IO.output_menu(menu=MENU)

    #Stores menu selection from user
    menu_choice = IO.input_menu_choice()
    
    # Input user data and store it to table
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)

    #Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
    #Exits the loop and ends the program
    elif menu_choice == "4":
        break
    #For invalid entry
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
