from tkinter import *

class Converter:

  def __init__(self):

    button_font = ("Arial 16 bold")
    button_fg = "#FFFFFF"

    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.temp_heading = Label(self.temp_frame,
                             text="Capital City Quiz",
                             font=("Arial 16 bold"))
    
    self.temp_heading.grid(row=0)

    instructions = "Please select an action" \
                   "then press one of the buttons " \
                   "to take the quiz"

    self.temp_instructions = Label(self.temp_frame,
                                  text=instructions)
    self.temp_instructions.grid(row=1)

    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.start_button = Button(self.button_frame,
                              text="START QUIZ",
                              bg="#9C0000",
                              fg=button_fg,
                              font=button_font, width=12)
    self.start_button.grid(row=0, column=0, padx=5, pady=5)

    self.instruct_button = Button(self.button_frame,
                              text="INSTRUCTIONS",
                              bg="#990099",
                              fg=button_fg,
                              font=button_font, width=12)
    self.instruct_button.grid(row=0, column=1, padx=5, pady=5)

    self.history_button = Button(self.button_frame,
                              text="HISTORY",
                              bg="#009900",
                              fg=button_fg,
                              font=button_font, width=12)
    self.history_button.grid(row=1, column=0, padx=5, pady=5)

    self.history_button = Button(self.button_frame,
                              text="HISTORY",
                              bg="#009900",
                              fg=button_fg,
                              font=button_font, width=12)
    self.history_button.grid(row=1, column=0, padx=5, pady=5)

    
    

 
                    

    
#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  Converter()
  root.mainloop()