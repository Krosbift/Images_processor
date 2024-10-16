import tkinter as tk

class TitleLabelComponent(tk.Label):
  def __init__(self, window):
    self.window = window
    self.init_config()

  def init_config(self):
    super().__init__(self.window, text="Visor de imágenes", font=("Helvetica", 16))
    self.pack(side="top", pady=10)
