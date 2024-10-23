from tkinter import ttk

class LabelScaleSpinboxFrameComponent(ttk.Frame):

  def __init__(self, controller, relx, rely):
    self.controller = controller
    self.relx = relx
    self.rely = rely
    self._configure_frame()
    self._bind_events()

  def _configure_frame(self):
    super().__init__(self.controller.parent_controller.component)
    self.configure(style="Custom.TFrame")
    self.place(relx=self.relx, rely=self.rely, relwidth=2, relheight=0.1, anchor="n")

  def _bind_events(self):
    self.controller.parent_controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=self.relx, rely=self.rely, relwidth=2, relheight=0.1, anchor="n")
