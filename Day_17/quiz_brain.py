# TODO Ask questions
# TODO Check if the answer is right
# Check if you are at the end of the quiz

# q_num = 0
# q_list = []
# method:
# next_question()

class Quiz:
    def __init__(self, q_list):
        self.q_num = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.q_num < len(self.question_list):
            return True
        else:
            False

    # or: def still_has_questions(self):
    #       return self.q_num < len(self.question_list):

    def next_question(self):
        current_question = self.question_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q {self.q_num}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower:
            self.score += 1
            print("You got it right")
        else:
            print("You got it right")
        print(f"Your score is {self.score}")


