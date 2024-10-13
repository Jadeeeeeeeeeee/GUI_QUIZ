from tkinter import *
from functools import partial

class Converter:

  def __init__(self):

    self.quiz_frame = Frame(padx=10, pady=10)
    self.quiz_frame.grid()

    self.quiz_heading = Label(self.quiz_frame,
                             text="Capital City Quiz",
                             font=("Arial bold 16"))

    self.quiz_heading.grid(row=0)

#main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Capital City Quiz")
  root.mainloop()