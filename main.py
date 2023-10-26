from func_list import *
def main():
    on = True
    while on:
        print("Hello, welcome to are you smarter than a 5th grade, please select on of the following options")
    
        print("1. Add a user")
        print("2. Take a quiz")
        print("3. update user")
        print("4. Exit application")
        user_input = input("What is your option?: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            
        else:
            print("Input contains characters.")
            continue

        if user_input == 4:
            on = False
        elif user_input == 3:
            pass
        elif user_input == 2:
            print("Welcome to are you smarter than a 5th grade")
            quiz_size = int(input("How many questions would you like your quiz to have?"))
            quiz_num = rand_num(quiz_size)

                
        elif user_input == 1:
            username = input("What is your username?: ")
            print(add_user(username))
            
            
        else:
            print("Sorry that is not a valid option")
    
    

if __name__ == "__main__":
    main()