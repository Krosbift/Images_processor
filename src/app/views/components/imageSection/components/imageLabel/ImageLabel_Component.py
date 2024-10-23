import tkinter as tk

class ImageLabelComponent(tk.Label):
  
  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, highlightthickness=1)
    self.place(anchor="e")

  def on_resize(self, _):
    self.place_configure(anchor="e")

  def update_image(self):
    self.config(image=self.controller.image)
    self.update()
