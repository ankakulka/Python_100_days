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

    def next_question(self):
        current_question = self.question_list[self.q_num]
        self.q_num += 1
        input(f"Q {self.q_num}: {current_question.text} (True/False): ")

