import csv
import db_base as DB
import functions as funct


class QuizDB(DB.DBbase):
    def __init__(self, db_name):
        super().__init__(db_name)

    def reset_database(self):
        """
        This function drops the existing tables if they exist and creates the following tables:
        - User: Stores user information.
        - Questions: Stores information about questions and their correct answers.
        - Result: Stores user results for exams.
        - Exam: Stores individual exam results.
        """
        sql_string = """
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Result;
        DROP TABLE IF EXISTS Exam;
        DROP TABLE IF EXISTS Questions;

        CREATE TABLE User (
            User_ID INTEGER PRIMARY KEY,
            User_Name TEXT NOT NULL,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,
            Email_ID TEXT UNIQUE NOT NULL,
            DOB DATE,
            Password TEXT NOT NULL);
            

        CREATE TABLE Questions (
            Question_no INTEGER PRIMARY KEY,
            Question TEXT NOT NULL,
            Option1 TEXT NOT NULL,
            Option2 TEXT NOT NULL,
            Option3 TEXT NOT NULL,
            Option4 TEXT NOT NULL,
            Correct_Ans TEXT NOT NULL);

        CREATE TABLE Result (
            Report_No INTEGER PRIMARY KEY,
            User_ID INTEGER,
            User_Name TEXT NOT NULL,
            Results TEXT NOT NULL,
            FOREIGN KEY (User_ID) REFERENCES User(User_ID));

        CREATE TABLE Exam (
            Result_ID INTEGER PRIMARY KEY,
            Question_No INTEGER,
            Correct_Ans TEXT,
            user_answer TEXT,
            Result INTEGER,
            FOREIGN KEY (Question_No) REFERENCES Questions(Question_no));
        """
        self.execute_script(sql_string)

    # def user_insert_values(self):
    #     # This function is a wrapper for the 'insert_user' method and allows for inserting user information
    #     # into the 'User' table.
    #     funct.insert_values(self)

    def insert_user(self, user_name, first_name, last_name, email_id, dob, password):
        # Insert a new user's information into the 'User' table.
        # This method inserts the provided user information into the 'User' table, and the changes are committed to the database.
        self._cursor.execute("INSERT INTO User (User_Name, First_Name, Last_Name, Email_ID, DOB, Password) VALUES (?, ?, ?, ?, ?, ?)",
                             (user_name, first_name, last_name, email_id, dob, password))
        self._conn.commit()
    def update_user(self, user_name, first_name=None, last_name=None, email_id=None, dob=None):
        """
        This method allows you to update user information in the 'User' table, such as first name, last name,
        email ID, and date of birth. You can specify which fields to update by providing their new values.
        """
        query = "UPDATE User SET "
        data = []

        if first_name:
            query += "First_Name = ?, "
            data.append(first_name)
        if last_name:
            query += "Last_Name = ?, "
            data.append(last_name)
        if email_id:
            query += "Email_ID = ?, "
            data.append(email_id)
        if dob:
            query += "DOB = ?, "
            data.append(dob)
        query = query[:-2]
        query += " WHERE User_Name = ?"
        data.append(user_name)
        self._cursor.execute(query, tuple(data))
        self._conn.commit()

    def delete_user(self, user_id):
        # This method allows you to delete a user's information from the 'User' table by specifying the user's unique User_ID.
        self._cursor.execute("DELETE FROM User WHERE User_ID = ?", (user_id,))
        self._conn.commit()

    def insert_questions(self, csv_path):
        # This method reads questions and their options from a CSV file and inserts them into the 'Questions' table
        # in the database.
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self._cursor.execute(
                    "INSERT INTO Questions (Question, Option1, Option2, Option3, Option4, Correct_Ans) VALUES (?, ?, ?, ?, ?, ?)",
                    (row[1], row[2], row[3], row[4], row[5], row[6]))
        self._conn.commit()

    def update_question(self, question_no, question=None, option1=None, option2=None, option3=None, option4=None,
                        correct_ans=None):
        # This method allows you to update a question and its options in the 'Questions' table based on its unique Question_no.
        # You can specify which fields to update by providing their new values.

        query = "UPDATE Questions SET "
        data = []
        if question:
            query += "Question = ?, "
            data.append(question)
        if option1:
            query += "Option1 = ?, "
            data.append(option1)
        if option2:
            query += "Option2 = ?, "
            data.append(option2)
        if option3:
            query += "Option3 = ?, "
            data.append(option3)
        if option4:
            query += "Option4 = ?, "
            data.append(option4)
        if correct_ans:
            query += "Correct_Ans = ?, "
            data.append(correct_ans)
        query = query[:-2]
        query += " WHERE Question_no = ?"
        data.append(question_no)
        self._cursor.execute(query, tuple(data))
        self._conn.commit()

    def delete_question(self, question_no):
        # This method allows you to delete a question and its associated options from the 'Questions' table.
        self._cursor.execute("DELETE FROM Questions WHERE Question_no = ?", (question_no,))
        self._conn.commit()

    def username_exists(self, username):
        # Query the database to check if the username exists in the User table
        query = "SELECT 1 FROM User WHERE User_Name = ?"
        self._cursor.execute(query, (username,))
        result = self._cursor.fetchone()

        if result:
            return True
        else:
            return False
        
    def password_check(self, username, password_guess):
        # This function is used to check if the password the user put in is the same as in the database
        query = "SELECT Password FROM User WHERE User_Name = ?"
        self._cursor.execute(query, (username,))
        result = self._cursor.fetchone()

        if result and password_guess == result[0]:
            return True
        else:
            return False
               
    def quiz_maker(self, quiz_size):
        # this method pulls random questions from the questions DB to create and administer each quiz.
        # this method is referenced in the UI when "take a quiz" is selected
        self.User_name = input("Please Enter User Name before entering to exam :")
        self.password = input("Please Enter password before entering to exam :")
        if self.username_exists(self.User_name) and self.password_check(self.User_name, self.password):
            # Username exists in the database
            quiz_num = funct.rand_num(quiz_size)
            print("")  # Spacer for the console window
            quiz_num = funct.rand_num(quiz_size)

            for num in quiz_num:
                answer = None
                result =0
                try:
                    while True:
                    # Fetching the questions
                        self._cursor.execute("SELECT Question FROM Questions WHERE Question_no = ?", (num,))
                        question = self._cursor.fetchall()[0][0]
                    # Fetching the options
                        self._cursor.execute(
                        "SELECT Option1, Option2, Option3, Option4 FROM Questions WHERE Question_no = ?", (num,))
                        options = self._cursor.fetchall()[0]

                        print(question)
                        print(options[0])
                        print(options[1])
                        print(options[2])
                        print(options[3])

                        answer= input(
                            "Please enter the letter that corresponds to the correct answer: ").upper()  # Ask the user to input what they think the answer is and makes sure it's upper case

                        self._cursor.execute("SELECT Correct_Ans FROM Questions WHERE Question_no = (?)",
                                         (num,))  # retrieve the correct answer
                        correct_ans = self.get_cursor.fetchone()

                        if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':  # checks to make sure that the user has entered a valid option

                            if answer == correct_ans[0]:
                                result = 1
                                print(input("Correct! Press Enter to continue."))
                                break

                            else:
                                result = 0
                                print(input("Incorrect. Press Enter to continue."))
                                break
                        else:
                            print("Please enter a valid letter option (A, B, C, or D).")
                            print("")  # spacer for console window


                except Exception as e:
                    print(e)

                finally:
                    self._cursor.execute(
                        "INSERT INTO Exam (Question_No, Correct_Ans) SELECT Question_No, Correct_Ans FROM Questions WHERE Question_no = (?)",
                        (num,))  # populates Exam table with question number and correct answer from the Questions table
                    self._cursor.execute("UPDATE Exam SET user_answer = (?) WHERE Question_no = (?)",
                                     (answer, num))  # populates user answers to Exam table
                    self._cursor.execute("UPDATE Exam SET Result = (?) WHERE Question_no = (?)",
                                     (result, num))  # populate the result column of the Exam table
                    self._conn.commit()   
            return True
        else:
            print("Username or Password is incorrect or Username does not exsist.")
            return False
            
            
        

    def quiz_grader(self,quiz_number):
        # this method grades quizes and is referenced in the UI when "take a quiz" is selected
        try:
            query = f"SELECT Result FROM Exam ORDER BY rowid DESC LIMIT {quiz_number};"
            self._cursor.execute(query)  # selecting results column from exam table
            results = self._cursor.fetchall()  # fetching results list
            # results_sum = sum([sum(i) for i in results])  # summing total points
            results_sum = sum([sum(i) for i in results])
            self.grade = (results_sum / len(results)) * 100  # calculating grade percentage
            print(f"{self.User_name} You scored {self.grade}%")
            print(input("Press Enter to continue."))

        except Exception as e:
            print(e)
        

class Person:
    def __init__(self, db):
        self.db = db
        self.user_name = input("What is your username: ")
        self.first_name = input("What is your first name: ")
        self.last_name = input("What is your last name: ")
        self.email_id = input("What is your email: ")
        self.dob = input("When is your birthday (DD-MM-YYYY): ")
        self.password = input("What is your password: ")
        db.insert_user(self.user_name, self.first_name, self.last_name, self.email_id, self.dob, self.password)

    def get_user_first(self):
        return self.first_name
            
