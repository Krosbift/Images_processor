import tkinter as tk

class FileLabelComponent(tk.Label):

  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind('<Configure>', self.on_resize)

  def init_config(self):
    super().__init__(self.section, text="Archivo de imagen: ", fg="#000000", bg="#FFFFFF", font=("Helvetica", 12))
    self.place(relx=0.10, rely=0.5, anchor="e")

  def on_resize(self, event):
    self.config(font=("Helvetica", min(12, int(event.height / 2))))
    self.place_configure(x=self.winfo_width() / 2 + 10, rely=0.5, anchor="e")
