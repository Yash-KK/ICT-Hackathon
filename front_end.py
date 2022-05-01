from tkinter import *
from quiz_format import QBrain
THEME_COLOR = "#375362"


class QUizInterface:
    def __init__(self,quiz_b:QBrain):
        self.quiz_b = quiz_b
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        # Label
        self.score_label = Label(text="Score:0",bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hello People",
            fill=THEME_COLOR,
            font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_b.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_b.score}")
            q_text = self.quiz_b.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have Reached the End of the QUIZ")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        is_right = self.quiz_b.check_answer("True")
        self.giving_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_b.check_answer("False")
        self.giving_feedback(is_right)

    def giving_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)