from tkinter import ttk

class HomeFrameComponent(ttk.Frame):

  def __init__(self, controller):
    self.controller = controller
    self._configure_frame()
    self._bind_events()

  def _configure_frame(self):
    super().__init__(self.controller.parent_controller.windowTk)
    self.configure(style='TFrame')
    self.pack(fill='both', expand=True)

  def _bind_events(self):
    self.controller.parent_controller.windowTk.bind("<Configure>", self._on_resize)

  def _on_resize(self, event):
    self.configure(width=event.width, height=event.height)
