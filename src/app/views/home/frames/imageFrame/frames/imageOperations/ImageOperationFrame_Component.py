import tkinter as tk

class ImageOperationFrameComponent(tk.Frame):
  
  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, bg="#FFFFFF")
    self.place(relx=0.7, y=0, relwidth=0.3, relheight=1, anchor="nw")

  def on_resize(self, _):
    self.place_configure(relx=0.7, y=0, relwidth=0.3, relheight=1, anchor="nw")
