import tkinter as tk

class BrightnessFrameComponent(tk.Frame):
  
  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, bg="#FFFFFF")
    self.place(relx=0.01, rely=0.005, relwidth=2, relheight=0.1, anchor="n")

  def on_resize(self, _):
    self.place_configure(relx=0.01, rely=0.005, relwidth=2, relheight=0.1, anchor="n")