import tkinter as tk

class TitleLabelComponent(tk.Label):

  def __init__(self, controller, window):
    self.controller = controller
    self.window = window
    self.init_config()
    self.window.bind('<Configure>', self.on_resize)

  def init_config(self):
    super().__init__(self.window, text="Visor de imágenes", font=("Helvetica", 20), fg="#8B0000")
    self.place(relx=0.5, y=20, anchor='n')

  def on_resize(self, _):
    self.place_configure(relx=0.5, y=20)
