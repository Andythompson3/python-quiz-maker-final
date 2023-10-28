import csv
import db_base as DB
import functions as funct
class QuizDB(DB.DBbase):
    def __init__(self, db_name):
        super().__init__(db_name)

    def reset_database(self):
        sql_string = """
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Result;
        DROP TABLE IF EXISTS Exam;
        DROP TABLE IF EXISTS Questions;

        CREATE TABLE User (
            User_ID INTEGER PRIMARY KEY,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,
            Email_ID TEXT UNIQUE NOT NULL,
            DOB DATE);

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
            Results TEXT NOT NULL,
            FOREIGN KEY (User_ID) REFERENCES User(User_ID));

        CREATE TABLE Exam (
            Result_ID INTEGER PRIMARY KEY,
            Question_No INTEGER,
            Correct_Ans TEXT,
            user_answer TEXT,
            Result TEXT,
            FOREIGN KEY (Question_No) REFERENCES Questions(Question_no));
        """
        self.execute_script(sql_string)

    def user_insert_values(self):
        funct.insert_values(self)
    def insert_user(self, first_name, last_name, email_id, dob):
        self._cursor.execute("INSERT INTO User (First_Name, Last_Name, Email_ID, DOB) VALUES (?, ?, ?, ?)",
                             (first_name, last_name, email_id, dob))
        self._conn.commit()

    def update_user(self, user_id, first_name=None, last_name=None, email_id=None, dob=None):
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
        query += " WHERE User_ID = ?"
        data.append(user_id)
        self._cursor.execute(query, tuple(data))
        self._conn.commit()

    def delete_user(self, user_id):
        self._cursor.execute("DELETE FROM User WHERE User_ID = ?", (user_id,))
        self._conn.commit()

    def insert_questions(self, csv_path):
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
        self._cursor.execute("DELETE FROM Questions WHERE Question_no = ?", (question_no,))
        self._conn.commit()