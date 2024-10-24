from tkinter import *

class quiz_Gui:

  def __init__(self):

    button_font = ("Arial 16 bold")
    button_fg = "#000000"

    self.quiz_frame = Frame(padx=10, pady=10)
    self.quiz_frame.grid()

    self.GUI_heading = Label(self.quiz_frame,
       text="Capital City Quiz",
       font=("Arial 16 bold"))

    self.GUI_heading.grid(row=0)

    question = "What is the capital of France?"

    self.quiz_question = Label(self.quiz_frame,
                                  text=question,
                                  wraplength=250,
                                  width=40,
                                  justify="left")
    self.quiz_question.grid(row=1)


    self.result_correct = Label(self.quiz_frame,
                               text = "Correct!",
                               fg="#008000")

    self.result_correct.grid(row=2)                         

    self.button_frame = Frame(self.quiz_frame)
    self.button_frame.grid(row=4)

    self.choice_a_button = Button(self.button_frame,
                              text="A.Berlin",
                              bg="#DAE8FC",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_a_button.grid(row=0, column=0, padx=5, pady=5)

    self.choice_b_button = Button(self.button_frame,
                              text="B.Kabul",
                              bg="#C3ABD0",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_b_button.grid(row=0, column=1, padx=5, pady=5)

    self.choice_c_button = Button(self.button_frame,
                              text="C.Rome",
                              bg="#FFB366",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_c_button.grid(row=1, column=0, padx=5, pady=5)

    self.choice_d_button = Button(self.button_frame,
                              text="D.Paris",
                              bg="#F8CECC",
                              fg=button_fg,
                              font=button_font, width=12)
    self.choice_d_button.grid(row=1, column=1, padx=5, pady=5)

    self.result_incorrect = Label(self.quiz_frame,
                                  text= "Incorrect!",
                                  fg="#FF0000")
    self.result_incorrect.grid(row=5)





if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  quiz_Gui()
  root.mainloop()