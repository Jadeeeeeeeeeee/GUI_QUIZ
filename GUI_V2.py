from tkinter import *
from functools import partial

class GUI:

  def __init__(self):

    button_font = ("Arial 16 bold")
    button_fg = "#000000"

    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.temp_heading = Label(self.temp_frame,
                             text="Capital City Quiz",
                             font=("Arial 16 bold"))

    self.temp_heading.grid(row=0)

    instructions = "Please select the actions you would like to do. Click start " \
                   "to start the quiz, instructions for instructions history to" \
                   "view previous quiz results, exit to exit the program"


    self.temp_instructions = Label(self.temp_frame,
                                  text=instructions,
                                  wraplength=300,
                                  width=40,
                                  justify="left")
    self.temp_instructions.grid(row=1)

    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.start_button = Button(self.button_frame,
                              text="Start Quiz",
                              bg="#DAE8FC",
                              fg=button_fg,
                              font=button_font, width=10)
    self.start_button.grid(row=0, column=0, padx=5, pady=5)

    self.history_button = Button(self.button_frame,
                              text="History",
                              bg="#FFB366",
                              fg=button_fg,
                              font=button_font, width=10)
    self.history_button.grid(row=1, column=0, padx=5, pady=5)

    self.quit_button = Button(self.button_frame,
                              text="Quit/Exit",
                              bg="#F8CECC",
                              fg=button_fg,
                              font=button_font, width=10)
    self.quit_button.grid(row=1, column=1, padx=5, pady=5)

    self.to_instruct_button = Button(self.button_frame,
                           text="Instructions",
                           bg="#C3ABD0",
                           fg=button_fg,
                           font=button_font, width=10, command=self.to_instruct)

    self.to_instruct_button.grid(row=0, column=1, padx=5, pady=5)

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

    help_text = "To use the program, simply enter the temperature " \
    "you wish to convert and then choose convert " \
    "to either degrees Celcius(centigrade) or " \
    "Fahrenheit.. \n\n" \
    "Note that -273 degrees C " \
    "(-459) is absulute zero (the coldest possible " \
    "temperature). If you try to convert a " \
    "temperature that is less than -273 degrees C, " \
    "you will get an error message. \n\n" \
    "To see your" \
    "calculation history and export it into a text " \
    "file, please click the 'History / Export' button"

    self.instructions_text_label = Label(self.instructions_frame, bg=backround,
                                text=help_text, wraplength=350, justify="left")

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
  GUI()
  root.mainloop()
