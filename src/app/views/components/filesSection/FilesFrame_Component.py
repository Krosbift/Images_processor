import tkinter as tk

class FilesFrameComponent(tk.Frame):
  
  def __init__(self, controller, window):
    self.controller = controller
    self.window = window
    self.init_config()
    self.window.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.window, bg=self.window.cget('bg'), highlightbackground="black", highlightthickness=1)
    self.place(relx=0.5, y=70, relwidth=0.8, relheight=0.07, anchor="n")

  def on_resize(self, _):
    self.place_configure(relx=0.5, y=70, relwidth=0.8, relheight=0.07)
