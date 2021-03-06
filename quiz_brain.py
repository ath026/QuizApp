import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.question.text)
        return 'Q.{}:{}'.format(self.question_number, q_text)
        # user_answer = input('Q.{}:{} true/False'.format(self.question_number, q_text))
        # self.check_answer(user_answer.lower(), question.answer.lower())

    def check_answer(self, user_answer):
        correct_answer=self.question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
