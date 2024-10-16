import tkinter as tk

class WindowTk(tk.Tk):

  def __init__(self):
    super().__init__()
    self.init_config()

  def init_config(self):
    self.title("Visor de imágenes")
    self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
