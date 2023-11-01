class Person:
    #This is the class that is going to create the user.
    def __init__(self, username, name, surname, birthdate, telephone, email):
        self.username = username
        self.first_name = name
        self.last_name = surname
        self.birthday = birthdate
        self.phone_number = telephone
        self.email = email