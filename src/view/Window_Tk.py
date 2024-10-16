import tkinter as tk
from .Window_Controller import WindowController

class WindowTk(tk.Tk):
  windowController: WindowController

  def __init__(self, controller: WindowController):
    super().__init__()
    self.windowController = controller
    self.init_config()

  def init_config(self):
    self.title("Visor de imágenes")
    self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
