from tkinter import *
import random



class quiz_Gui:



  def generate_question(self,question):

                        

    country = ["France", "Jamaica", "Italy", "Slovakia", "Japan", "Malaysia", 
"Croatia", "Indonesia", "Greece", "Switzerland"]

    right_answer = ["Paris", "Kingston", "Rome", "Bratislava", "Tokyo", "Kuala lumpur",
"Zagreb", "Jakarta", "Athens", "Bern"]

    option_1 = ["Berlin", "Madrid", "Manila", "Dubai", "Seoul", "Wellington", "Sydney", 
"Canberra", "Manama", "Gaborone"]

    option_2 = ["San Jose", "Djibouti", "London", "Reykjavik", "Dublin", "Tripoli", 
"Monaco","Moscow", "Victoria", "Damascus"]

    option_3 = ["Lisbon", "Cairo", "Helsinki", "Oslo", "Hanoi", "Ottawa",
                                            "Brasilia", "Bangkok", "Stockholm", "Luxembourg"]

    button_font = ("Arial 16 bold")
    button_fg = "#000000"

    global question_number,score 
                            
    score = 0
    question_number = 0 
                            
                            
    options = [right_answer[question_number]], option_1[question_number],option_2
[question_number]
         

                            
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





if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  quiz_Gui()
  root.mainloop()