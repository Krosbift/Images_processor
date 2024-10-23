import tkinter as tk

class FileLabelComponent(tk.Label):

  def __init__(self, controller):
    self.controller = controller
    self._configure_label()
    self._bind_events()

  def _configure_label(self):
    super().__init__(
      self.controller.component,
      text="Archivo de imagen: ",
      fg="#000000",
      bg="#FFFFFF",
      font=("Helvetica", 12)
    )
    self.place(relx=0.1, rely=0.5, anchor="e")

  def _bind_events(self):
    self.controller.component.bind('<Configure>', self._on_resize)

  def _on_resize(self, event):
    self.config(font=("Helvetica", min(12, int(event.height / 2))))
    self.place_configure(x=self.winfo_width() / 2 + 10, rely=0.5, anchor="e")
