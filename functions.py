import random
def insert_values(db_instance):
    #This is a function that asks users to put in user information and then it will call the class that creates an instance of the user class.
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email_id = input("What is your email: ")
    dob = input("When is your birthday (DD-MM-YYYY): ")
    db_instance.insert_user(first_name, last_name, email_id, dob)

