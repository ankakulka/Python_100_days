from question_model import Question
from data import question_data
from quiz_brain import Quiz

# Create q bank - a list of objects based on a Question class
# question_bank = [ Question(q1,a1),
#                 Question(q1,a1),
# ]
question_bank = []

# Convert a list of dictionaries into a list of objects based on the Question class
for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]
    # Set a new variable to the Question class with local variables as params
    new_question = Question(question_text, answer_text)
    # Now append objects created from the Question class to the question_bank list
    question_bank.append(new_question)

quiz = Quiz(question_bank)
quiz.next_question()

#if quiz has q remaining:
while quiz.still_has_questions():
    quiz.next_question()

