from tkinter import Tk, ttk, Frame

""" class Application(Frame):
  def createWidgets():
    self.something = 'something' """


class CustomApp(Tk):
  def start(self):
    self.geometry("600x400")
    self.mainloop()


def start_script():
  app = CustomApp()
  app.start()

if(__name__ == '__main__'):
  print("Ran as main module")
  start_script()