from tkinter import *
from functools import partial

if __name__ == "__main__":
  root = Tk()
  root.title("Temperature Converter")
  converter = Converter()
  root.mainloop()