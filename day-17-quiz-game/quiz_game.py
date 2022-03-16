# Main part of the game

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Stores question objects
question_bank = []

# Read individual dictionary items from question_data (data.py)
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Instantiate an object from Question class;
    new_question = Question(question_text, question_answer)

    # Add instantiated object to a list
    question_bank.append(new_question)

# Instantiate an object from QuizBrain class (quiz_brain.py) & pass the contents of question_bank as a parameter value
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    # Loads a question from question_bank
    quiz.next_question()

# Display congratulatory message
print("You've completed the quiz.")

# Display final score over total number of questions stored in question_bank
print(f"Your final score is {quiz.score}/{len(question_bank)}")
