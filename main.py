#imports
from tkinter import *
from functools import partial
import random 

#Set up the main GUI for the program
class main_GUI:

  def __init__(self, root):

    self.root = root
    #common button format and fonts
    button_font = ("Arial 16 bold")
    button_fg = "#000000"

    #clear saved history upon start up
    with open("quiz_history.txt", "w") as file:
      pass
    
    #Variable for tracking if history should be saved
    self.save_history = IntVar()
    #Make the main GUI frame
    self.GUI_frame = Frame(root, padx=10, pady=10)
    self.GUI_frame.grid()

    #heading label
    self.GUI_heading = Label(self.GUI_frame,
                             text="Capital City Quiz",
                             font=("Arial 16 bold"), )

    self.GUI_heading.grid(row=0)
    #Instructions
    Greetings = "Greetings!, please select the actions you would like to do. " 


    self.GUI_instructions = Label(self.GUI_frame,
                                  text=Greetings,
                                  wraplength=350,
                                  width=50,
                                  justify="left")
    self.GUI_instructions.grid(row=1)
    #Checkbox for saving quiz history
    self.save_history_checkbox = Checkbutton(self.GUI_frame, text="Save History", variable=self.save_history)
    self.save_history_checkbox.grid(row=2, sticky="w")

    #Create button frame
    self.button_frame = Frame(self.GUI_frame)
    self.button_frame.grid(row=4)

    #create buttons for different functions
    self.start_button = Button(self.button_frame,
                              text="Start",
                              bg="#DAE8FC",
                              fg=button_fg,
                              font=button_font, width=10, command=self.start_quiz)
    self.start_button.grid(row=0, column=0, padx=5, pady=5)

    self.history_button = Button(self.button_frame,
                              text="History",
                              bg="#FFB366",
                              fg=button_fg,
                              font=button_font, width=10, command=self.show_history)
    self.history_button.grid(row=1, column=0, padx=5, pady=5)

    self.quit_button = Button(self.button_frame,
                              text="Quit",
                              bg="#F8CECC",
                              fg=button_fg,
                              font=button_font, width=10,
                              command=self.root.destroy)
    self.quit_button.grid(row=1, column=1, padx=5, pady=5)

    self.to_instruct_button = Button(self.button_frame,
                           text="Instructions",
                           bg="#C3ABD0",
                           fg=button_fg,
                           font=button_font, width=10, command=self.to_instruct)

    self.to_instruct_button.grid(row=0, column=1, padx=5, pady=5)
  
  def to_instruct(self):
   DisplayInstructions(self)

  def start_quiz(self):
    quiz_Gui(self)

  def show_history(self):
    quiz_history()
 


class quiz_Gui:

  def __init__(self, partner):

    self.quiz_box = Toplevel()
    self.partner = partner
    
    partner.start_button.config(state=DISABLED)

    self.quiz_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_quiz, partner))


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

    self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
    self.quiz_frame.grid()

    self.GUI_heading = Label(self.quiz_frame,
       text="Capital City Quiz",
       font=("Arial 16 bold"))

    self.GUI_heading.grid(row=0)

    self.quiz_question = Label(self.quiz_frame,
                                  text="",font="Arial 12",
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

    self.result = Label(self.quiz_frame,
                          text = "")
    self.result.grid(row=2)                        

    self.score_label = Label(self.quiz_frame, text="Score: 0",
                             font=button_font)
    self.score_label.grid(row=3)                        


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
        self.result.config(text="Correct!", fg="#008000")  
        self.score += 1
    else:
        self.result.config(text=f"Incorrect!, the right answer is {self.right_answer[self.question_number]}", fg="#FF0000")

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

       if self.partner.save_history.get() == 1:
         with open("quiz_history.txt", "a") as file:
           file.write(f"Score: {self.score}\n")

       self.exit_button = Button(self.button_frame, font=("Arial 16 bold"),
                                 text="Exit", bg="#FF3333", fg="#FFFFFF", width=10,
                                 command=partial(self.close_quiz, self.partner))
       self.exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

  def close_quiz(self, partner):
    partner.start_button.config(state=NORMAL)
    self.quiz_box.destroy()

  

class quiz_history:
  def __init__(self):
    self.history_box = Toplevel()
    self.history_box.title("Quiz History")

    Label(self.history_box, text="Quiz History", font=("Arial 14 bold")).pack(pady=10)

    self.history_text = Text(self.history_box, wrap="word", width=30, height=15)
    self.history_text.pack(pady=10)

    self.load_history()

  def load_history(self):
    try:
      with open("quiz_history.txt", "r") as file:
        history = file.read().strip()
        message = history if history else "No history available yet."
    except FileNotFoundError:
      message = "No history available yet"

    self.history_text.insert("1.0", message)

class DisplayInstructions:


  def __init__(self, partner):
    #setup dialogue box and backround colour
    backround = "#FFCFAB"

    self.instructions_box = Toplevel()

    #disable help button
    partner.to_instruct_button.config(state=DISABLED)

    #If users press cross at top, closses help and
    #'releases' help button
    self.instructions_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_instructions, partner))

    self.instructions_frame = Frame(self.instructions_box, width=300, height=200,
                           bg=backround)
    self.instructions_frame.grid()

    self.instructions_heading_label = Label(self.instructions_frame, bg=backround,
                                   text="Intructions",font="Arial 14 bold")

    self.instructions_heading_label.grid(row=0)

    instruction_text ='''     Functions of the four buttons in the main GUI 
     -the start quiz button: Starts the quiz 
     -the instructions button: Displays the instructions
     -the history button: Displays the history of the quiz
     -the quit button: Exits the program
     -the tickbox for saving history:
      when ticked: saves hisotry and makes another file 
      with the history in it
      not ticked: doesn't save history
      Please enjoy using the program!'''


    self.instructions_text_label = Label(self.instructions_frame, bg=backround,
                                text=instruction_text, wraplength=350, width=50, justify="left")

    self.instructions_text_label.grid(row=1, padx=10)

    self.dismiss_button = Button(self.instructions_frame, font=("Arial 12 bold"), 
                                text="Dismiss", bg="#CC6000", fg="#FFFFFF",
                                command=partial(self.close_instructions, partner)) 
    self.dismiss_button.grid(row=2, padx=10, pady=10)

  def close_instructions(self, partner):
    #Put help button back to normal...
    partner.to_instruct_button.config(state=NORMAL)
    self.instructions_box.destroy()

#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  main_GUI(root)
  root.mainloop()