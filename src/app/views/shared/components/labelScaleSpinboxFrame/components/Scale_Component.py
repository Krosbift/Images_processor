from tkinter import ttk

class ScaleComponent(ttk.Scale):

  def __init__(self, controller, command):
    self.controller = controller
    self.command = command
    self._configure_styles()
    self._configure_scale()
    self._bind_events()

  def _configure_scale(self):
    super().__init__(self.controller.component, orient="horizontal", length=100, from_=0, to=1, command=self.command)
    self.place(relx=0.1, rely=0.5, anchor="e")

  def _configure_styles(self):
    style = ttk.Style()
    style.configure("TScale", background="#ffffff", troughcolor="#666666", sliderthickness=0, troughrelief="flat", sliderrelief="raised", sliderlength=1)

  def _bind_events(self):
    self.controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, event):
    self.config(length=event.width * 0.15)
    self.place_configure(relx=0.97, rely=0.5, relheight=0.6, anchor="e")