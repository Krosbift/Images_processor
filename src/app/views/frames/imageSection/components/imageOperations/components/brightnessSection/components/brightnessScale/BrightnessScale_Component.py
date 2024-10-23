from tkinter import ttk

class BrightnessScaleComponent(ttk.Scale):
  
  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)

  def init_config(self):
    super().__init__(self.section, orient="horizontal", length=100, from_=0, to=1, command=self.on_scale_move)
    style = ttk.Style()
    style.configure("TScale",
      background="#ffffff",
      troughcolor="#666666",
      sliderthickness=0,
      troughrelief="flat",
      sliderrelief="raised",
      sliderlength=1)
    self.place(relx=0.97, rely=0.5, relheight=0.6, anchor="e")

  def on_resize(self, event):
    self.config(length=event.width * 0.15)
    self.place_configure(relx=0.97, rely=0.5, relheight=0.6, anchor="e")

  def on_scale_move(self, value):
    self.controller.parent_controller.childrenControllers['BrightnessSpinBoxController'].set_value(value)
