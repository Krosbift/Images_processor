from tkinter import ttk

class FileLabelComponent(ttk.Label):

  def __init__(self, controller):
    self.controller = controller
    self._configure_label()
    self._bind_events()

  def _configure_label(self):
    super().__init__(
      self.controller.component,
      text="Archivo de imagen: ",
      style="FileLabel.TLabel"
    )
    self.place(relx=0.1, rely=0.5, anchor="e")

  def _configure_styles(self):
    style = ttk.Style()
    style.configure("FileLabel.TLabel", foreground="#000000", background="#FFFFFF", font=("Helvetica", 12))
  
  def _bind_events(self):
    self.controller.component.bind('<Configure>', self._on_resize)

  def _on_resize(self, event):
    style = ttk.Style()
    new_font_size = min(12, int(event.height / 2))
    style.configure("FileLabel.TLabel", font=("Helvetica", new_font_size))
    self.place_configure(x=self.winfo_width() / 2 + 10, rely=0.5, anchor="e")
