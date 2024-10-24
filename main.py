from tkinter import *
import random


class quiz_Gui:

  def __init__(self, root):

    self.score = 0
    self.question_number = 0                        

    self.country = ["France", "Jamaica", "Italy", "Slovakia", "Japan", "Malaysia", 
"Croatia", "Indonesia", "Greece", "Switzerland"]

    self.right_answer = ["Paris", "Kingston", "Rome", "Bratislava", "Tokyo", "Kuala lumpur",
"Zagreb", "Jakarta", "Athens", "Bern"]

    self.option_1 = ["Berlin", "Madrid", "Manila", "Dubai", "Seoul", "Wellington", "Sydney", 
"Canberra", "Manama", "Gaborone"]

    self.option_2 = ["San Jose", "Djibouti", "London", "Reykjavik", "Dublin", "Tripoli", 
"Monaco","Moscow", "Victoria", "Damascus"]

    self.option_3 = ["Lisbon", "Cairo", "Helsinki", "Oslo", "Hanoi", "Ottawa",
"Brasilia", "Bangkok", "Stockholm", "Luxembourg"]

    button_font = ("Arial 16 bold")
    button_fg = "#000000"


    self.quiz_frame = Frame(padx=10, pady=10)
    self.quiz_frame.grid()

    self.GUI_heading = Label(self.quiz_frame,
       text="Capital City Quiz",
       font=("Arial 16 bold"))

    self.GUI_heading.grid(row=0)

    self.quiz_question = Label(self.quiz_frame,
                                  text="",
                                  wraplength=250,
                                  width=40,
                                  justify="left")
    self.quiz_question.grid(row=1)

    self.button_frame = Frame(self.quiz_frame)
    self.button_frame.grid(row=4)

    self.choice_a_button = Button(self.button_frame,
                              text="",
                              bg="#DAE8FC",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_a_button.grid(row=0, column=0, padx=5, pady=5)

    self.choice_b_button = Button(self.button_frame,
                              text="",
                              bg="#C3ABD0",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_b_button.grid(row=0, column=1, padx=5, pady=5)

    self.choice_c_button = Button(self.button_frame,
                              text="",
                              bg="#FFB366",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_c_button.grid(row=1, column=0, padx=5, pady=5)

    self.choice_d_button = Button(self.button_frame,
                              text="",
                              bg="#F8CECC",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_d_button.grid(row=1, column=1, padx=5, pady=5)

    self.result_correct = Label(self.quiz_frame,
                          text = "",
                          fg="#008000")
    self.result_correct.grid(row=2)                        

    self.result_incorrect = Label(self.quiz_frame,
                                  text= "",
                                  fg="#FF0000")
    self.result_incorrect.grid(row=5)

    self.score_label = Label(self.quiz_frame, text="Score: 0",
                             font=button_font)                        


    self.generate_question()


  def generate_question(self):
    options = [self.right_answer[self.question_number], 
               self.option_1[self.question_number], 
self.option_2[self.question_number],self.option_3[self.question_number]]
    random.shuffle(options)  

    self.quiz_question.config(text=f"What is the capital of {self.country[self.question_number]}?")
    self.choice_a_button.config(text=f"A. {options[0]}", command=lambda:
                                self.check_answer(options[0]))
    self.choice_b_button.config(text=f"B. {options[1]}", command=lambda:
                               self.check_answer(options[1]))
    self.choice_c_button.config(text=f"C. {options[2]}", command=lambda:
                               self.check_answer(options[2]))
    self.choice_d_button.config(text=f"D. {options[3]}", command=lambda:
                                self.check_answer(options[3]))

  def check_answer(self, answer):
    if answer == self.right_answer[self.question_number]:
        self.result_correct.config(text="Correct!")  
        self.score += 1
    else:
        self.result_incorrect.config(text=f"Incorrect!, the right answer is {self.right_answer[self.question_number]}")

    self.score_label.config(text=f"Score: {self.score}")

    self.question_number += 1
    if self.question_number < len(self.country):
       self.generate_question()
    else:
       self.quiz_question.config(text="Quiz complete!") 
       self.choice_a_button.config(state=DISABLED)
       self.choice_b_button.config(state=DISABLED)
       self.choice_c_button.config(state=DISABLED)
       self.choice_d_button.config(state=DISABLED)



if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  quiz = quiz_Gui(root)
  root.mainloop()