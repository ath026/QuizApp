from tkinter import *

from QuizApp.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.title = 'Quiz'
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, )
        # score Entry
        self.score = Label(text='score:0', fg='white', font={"arial", 20, 'italic'}, bg=THEME_COLOR)
        self.score.grid(column=2, row=0)

        # canvas
        self.canvas = Canvas(height=250, width=300, bg='white')

        self.question_text = self.canvas.create_text(150, 125, width=250, text='some_question here',
                                                     font={"arial", 20, 'italic'})
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image,command=self.true_pressed)

        self.true_button.grid(row=3, column=1)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image,command=self.false_pressed)

        self.false_button.grid(row=3, column=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text='score:{}'.format(self.quiz.score))
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            q_text='You have reached end of the Quiz'
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(500,self.get_next_question)
