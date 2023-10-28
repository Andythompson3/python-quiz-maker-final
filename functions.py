import random
def insert_values(db_instance):
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email_id = input("What is your email: ")
    dob = input("When is your birthday (DD-MM-YYYY): ")
    db_instance.insert_user(first_name, last_name, email_id, dob)

