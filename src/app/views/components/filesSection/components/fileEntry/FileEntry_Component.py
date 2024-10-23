import tkinter as tk

class FileEntryComponent(tk.Entry):

  def __init__(self, controller, section):
    self.path_route = tk.StringVar()
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, font=("Helvetica", 10), bg="#FFFFFF", fg="#111111", bd=2, relief="solid", borderwidth=1, state="readonly", textvariable=self.path_route)
    self.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="center")

  def on_resize(self, _):
    self.place_configure(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="center")