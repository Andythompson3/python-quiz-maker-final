import random

def insert_values(db_instance):
    #This is a function that asks users to put in user information and then it will call the class that creates an instance of the user class.
    user_name= input("What is your username: ")
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email_id = input("What is your email: ")
    dob = input("When is your birthday (DD-MM-YYYY): ")
    db_instance.insert_user(user_name, first_name, last_name, email_id, dob)
    return first_name

#This is a function that will create a list of random numbers that will be used to pull questions from the database.
def rand_num(size):
    num_list = []
# Once the user put how many questions they want to add this will pick a random number for each slot.
    while len(num_list) < size:
        num = random.randint(1, 30)
#This will make sure that no numbers are added as a dublicate.
        if num not in num_list:
            num_list.append(num)
    return num_list

