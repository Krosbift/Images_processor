from tkinter import ttk

class TitleLabelComponent(ttk.Label):

  def __init__(self, controller):
    self.controller = controller
    self._configure_label()
    self._bind_events()

  def _configure_label(self):
    super().__init__(self.controller.component, text="Visor de imágenes", font=("Helvetica", 20), foreground="#8B0000")
    self.place(relx=0.5, y=20, anchor='n')

  def _bind_events(self):
    self.controller.component.bind('<Configure>', self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.5, y=20)
