import random
from classes import *

def rand_num(size):
    num_list = []
    for _ in range(size):
        num = random.randint(1, 30)  # Generates a random integer between 1 and 30 (inclusive)
        num_list.append(num)
    
    return (num_list)


def add_user(username):
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    birthday = input("When is your birthday (DD-MM-YYYY): ")
    phone_number = input("What is your phone number: ")
    email = input("What is your email: ")
    user = Person(username, first_name, last_name, birthday, phone_number, email)
    add_user_db(user)
    
def add_user_db(user):
    pass