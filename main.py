#from func_list import * # EC - this type of import (using the *) didn't work for me, so I imported as below - feel free to change back!
from functions import *
import Quiz_Database_code as qz

db = qz.QuizDB("quiz_db.sqlite")

# Questions
db.reset_database()
db.insert_questions("ProjQuestions.csv")


# db.update_question(1,correct_ans="B")
# db.delete_question(1)
# User
# db.user_insert_values()
# db.update_user(1, last_name="T")
# db.delete_user(1)

# Exam

def main():
    on = True
    while on:
        print("\nHello, welcome to are you smarter than a 5th grade, please select on of the following options")

        print("1. Add a user")
        print("2. Take a quiz")
        print("3. update user")
        print("4. View Result")
        print("5. Exit application")

        user_input = input("What is your option?: ")
        # checks if the users input is a number or not.
        if user_input.isnumeric():
            user_input = int(user_input)
        else:
            print("Input contains characters.")
            continue

            #  option if user wants to Add a user.
        if user_input == 1:
            person_instance = qz.Person(db)
            first_name = person_instance.get_user_first()
            print(f"{first_name}, your details have been updated.")

            # option if user wants to Take a quiz.
        elif user_input == 2:
            print("Welcome to are you smarter than a 5th grade")
            while True:
                quiz_size = input("How many questions would you like your quiz to have? (max 30): ")
                try:
                    quiz_size = int(quiz_size)
                    if 1 <= quiz_size <= 30:# Check if the input is within the desired range
                        break  # Valid input, exit the loop
                    else:
                        print("Number needs to be between 1 and 30")
                except ValueError:
                    print("Please enter a number.")
            quiz_maker = db.quiz_maker(quiz_size)
            if quiz_maker:
                db.quiz_grader(quiz_size)
            else:
                continue

            # option if user wants to update user.
        elif user_input == 3:
            update_user_name = input("What is the user name you would like to update?")
            update_first_name = input("What is your updated first name: ")
            if update_first_name is not None:
                pass

            update_last_name = input("What is your last name: ")
            if update_last_name.lower() is not None:
                pass

            update_email_id = input("What is your email: ")
            if update_email_id is not None:
                pass

            update_dob = input("When is your birthday (DD-MM-YYYY): ")
            if update_dob is not None:
                pass
            db.update_user(update_user_name, update_first_name, update_last_name, update_email_id, update_dob)

            print(f"{update_user_name}, your details have been updated.")
        # option if user wants to view results
        elif user_input ==4:
            User_name= input("Please Enter your user name: ")
            # if User_name is not None:
            #     # db.view_result(User_name)
            # else:
            #     # print("Please try again.")

            # option if user wants to Exit application.
        elif user_input == 5:
            on = False
            break

        else:
            # If the user puts in a number that is not between 1 and 4 they will get this reply.
            print("Sorry that is not a valid option")

    db.close_db()


if __name__ == "__main__":
    main()
