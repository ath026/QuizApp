from QuizApp.data import question_data
from QuizApp.question_model import Question
from QuizApp.quiz_brain import QuizBrain
from QuizApp.ui import QuizInterface

question_bank = []

for item in question_data:
    question_bank.append((Question(item["question"], item["correct_answer"])))

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
