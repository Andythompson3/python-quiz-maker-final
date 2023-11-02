# from func_list import * # EC - this type of import (using the *) didn't work for me, so I imported as below - feel free to change back! 
from functions import *
import Quiz_Database_code as qz
import Quiz_Database_code as qz





def main():
    on = True
    while on:
        
        db = qz.QuizDB("quiz_db.sqlite")
        # Questions
        db.reset_database()
        # db.insert_questions("ProjQuestions.csv")
        # db.update_question(1,correct_ans="B")
        # db.delete_question(1)
        # User
        # db.user_insert_values()
        # db.update_user(1, last_name="T")
        # db.delete_user(1)
        #Exam
        
        
        print("Hello, welcome to are you smarter than a 5th grade, please select on of the following options")
    
        print("1. Add a user")
        print("2. Take a quiz")
        print("3. update user")
        print("4. Exit application")

        user_input = input("What is your option?: ")
        # checks if the users input is a number or not.
        if user_input.isnumeric():
            user_input = int(user_input) 
        else:
            print("Input contains characters.")
            continue




            #  option if user wants to Add a user.
        if user_input == 1:
            username = input("What is your username?: ")
            print(insert_values(db))
            
            # option if user wants to Take a quiz.
        elif user_input == 2:
            print("Welcome to are you smarter than a 5th grade")
            
            db = qz.QuizDB("quiz_db.sqlite")
            
            db.quiz_maker()
            db.quiz_grader()
            
            # option if user wants to update user.
        elif user_input == 3:
            update_id = input("What is the ID you would like to update?")
            update_first_name = input("What is your updaetd first name: ")
            update_last_name = input("What is your last name: ")
            update_email_id = input("What is your email: ")
            update_dob = input("When is your birthday (DD-MM-YYYY): ")
            qz.update_user(update_id, update_first_name, update_last_name, update_email_id, update_dob)
        
            # option if user wants to Exit application.
        elif user_input == 4:
            on = False
            break 
         
        else:
            #If the user puts in a number that is not between 1 and 4 they will get this reply.
            print("Sorry that is not a valid option")
    
    db.close_db()
    

if __name__ == "__main__":
    main()
