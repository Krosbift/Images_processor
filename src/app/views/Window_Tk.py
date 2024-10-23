import tkinter as tk

class WindowTk(tk.Tk):

  def __init__(self, controller):
    self.controller = controller
    self._configure_tk()

  def _configure_tk(self):
    super().__init__()
    self.title("Visor de imágenes")
    self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
    self.state('zoomed')
    self.minsize(800, 600)
