import Quiz_Database_code as qz

db = qz.QuizDB("quiz_db.sqlite")

# Questions
db.reset_database()
# db.insert_questions("ProjQuestions.csv")
# db.update_question(1,correct_ans="B")
# db.delete_question(1)

# User
db.user_insert_values()
# db.update_user(1, last_name="T")
# db.delete_user(1)

#Exam

db.close_db()

