# Handles the questioning & quizzing functionality
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        # Get next question from the question_list at the current question_number
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Ask input from user
        input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
