import tkinter as tk

class WindowTk(tk.Tk):

  def __init__(self, controller):
    self.controller = controller
    self.init_config()

  def init_config(self):
    super().__init__()
    self.title("Visor de imágenes")
    self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
    self.state('zoomed')
    self.minsize(800, 600)
