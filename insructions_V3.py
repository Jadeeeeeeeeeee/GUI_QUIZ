from tkinter import *
from functools import partial

class Converter:

  def __init__(self):

    #common format for all buttons
    #Arial size 14 bold, with white text
    button_font = ("Arial 12 bold")
    button_fg = "#FFFFFF"

    # Set up the GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    #Conversion, help and history / export buttons
    self.button_frame = Frame(padx=30, pady=30)
    self.button_frame.grid(row=0)

    self.to_instruct_button = Button(self.button_frame,
                                   text="Help / Info",
                                   bg="#CC6600",
                                   fg=button_fg, width=12,
                                   font=button_font, command=self.to_instruct)
    self.to_instruct_button.grid(row=1, column=0, padx=5, pady=5)

  def to_instruct(self):
   DisplayInstructions(self)

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
                                   text="Help / Info",font="Arial 14 bold")

    self.instructions_heading_label.grid(row=0)

    help_text = '''     Functions of the four buttons in the main GUI 
     the start quiz button: Starts the quiz 
     the instructions button: Displays the instructions
     the history button: Displays the history of the quiz
     the quit button: Exits the program
     Please enjoy using the program'''
    
    self.instructions_text_label = Label(self.instructions_frame, bg=backround,
                                text=help_text, wraplength=350, justify="left")

    self.instructions_text_label.grid(row=1, padx=10)

    self.dismiss_button = Button(self.instructions_frame, font=("Arial 12 bold"), 
                                text="Dismiss", bg="#CC6000", fg="#FFFFFF",
                                command=partial(self.close_instructions, partner)) 
    self.dismiss_button.grid(row=2, padx=10, pady=10)

  def close_instructions(self, partner):
    #Put help button back to normal...
    partner.to_help_button.config(state=NORMAL)
    self.instructions_box.destroy()



#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  Converter()
  root.mainloop()
