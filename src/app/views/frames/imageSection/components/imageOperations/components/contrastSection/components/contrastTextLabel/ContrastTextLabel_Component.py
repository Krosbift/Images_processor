import tkinter as tk

class ContrastTextLabelComponent(tk.Label):

  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind('<Configure>', self.on_resize)

  def init_config(self):
    super().__init__(self.section, text="Contraste: ", fg="#000000", bg="#FFFFFF", font=("Helvetica", 12))
    self.place(relx=0.5, rely=0.5, anchor="w")

  def on_resize(self, event):
    self.place_configure(relx=0.5, rely=0.5, anchor="w")