# from func_list import * # EC - this type of import (using the *) didn't work for me, so I imported as below - feel free to change back! 
import func_list as fl
import Quiz_Database_code as qz

def main():
    on = True
    while on:
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
            print(add_user(username))
            
            # option if user wants to Take a quiz.
        elif user_input == 2:
            print("Welcome to are you smarter than a 5th grade")
            
            db = qz.QuizDB("quiz_db.sqlite")
            
            db.quiz_maker()
            db.quiz_grader()
            
            # option if user wants to update user.
        elif user_input == 3:
            pass
        
            # option if user wants to Exit application.
        elif user_input == 4:
            on = False
         
        else:
            #If the user puts in a number that is not between 1 and 4 they will get this reply.
            print("Sorry that is not a valid option")
    
    

if __name__ == "__main__":
    main()
