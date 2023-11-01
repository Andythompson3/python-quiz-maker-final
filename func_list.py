import random
from classes import *
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
#This is a function that asks users to put in user information and then it will call the class that creates an instance of the user class.
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    birthday = input("When is your birthday (DD-MM-YYYY): ")
    phone_number = input("What is your phone number: ")
    email = input("What is your email: ")
    user = Person(username, first_name, last_name, birthday, phone_number, email)
    add_user_db(user)
    
def add_user_db(user):
    pass