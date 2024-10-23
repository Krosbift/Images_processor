from tkinter import ttk

class FilesFrameComponent(ttk.Frame):
  
  def __init__(self, controller):
    self.controller = controller
    self._configure_frame()
    self._bind_events()

  def _configure_frame(self):
    super().__init__(self.controller.parent_controller.component)
    self.place(relx=0.5, y=70, relwidth=0.9, relheight=0.07, anchor="n")

  def _bind_events(self):
    self.controller.parent_controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.5, y=70, relwidth=0.9, relheight=0.07)