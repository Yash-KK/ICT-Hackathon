from model import Question
from info import information
from quiz_format import QBrain
from front_end import QUizInterface
question_list = []
for question in information:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)


quiz = QBrain(question_list)
quiz_ui = QUizInterface(quiz)

