import tkinter as tk

class ExploreButtonComponent(tk.Button):

  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, text="Explorar", font=("Helvetica", 10), bg="#E5E5E5", fg="#111111", bd=2, relief="solid", borderwidth=1, cursor="hand2", command=self.controller.parent_controller.get_file_path)
    self.place(relx=0.8, rely=0.5, relwidth=0.09, relheight=0.5, anchor="w")

  def on_resize(self, _):
    self.place_configure(relx=0.8, rely=0.5, relwidth=0.09, relheight=0.5, anchor="w")