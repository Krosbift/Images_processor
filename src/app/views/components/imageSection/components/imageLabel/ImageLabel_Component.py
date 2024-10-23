import tkinter as tk

class ImageLabelComponent(tk.Label):
  
  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, highlightthickness=1)
    self.place(x=0, y=0, relwidth=0.7, relheight=1, anchor="nw")

  def on_resize(self, _):
    self.place_configure(x=0, y=0, relwidth=0.7, relheight=1, anchor="nw")

  def update_image(self):
    self.config(image=self.controller.image)
    self.update()
