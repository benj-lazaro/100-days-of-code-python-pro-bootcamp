from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Will store question objects
question_bank = []

# Read individual items from question_data (data.py)
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Instantiate objects from Question class; pass retrieved "text" & "answer" values as parameters
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Instantiate an object from QuizBrain class & pass the object question_bank
quiz = QuizBrain(question_bank)

# Class the method .next_question() to load up the succeeding question
quiz.next_question()

