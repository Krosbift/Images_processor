from tkinter import ttk

class TextLabelComponent(ttk.Label):

  def __init__(self, controller, text, style_name):
    self.controller = controller
    self.text = text
    self.style_name = style_name
    self._configure_label()
    self._configure_styles()
    self._bind_events()

  def _configure_label(self):
    super().__init__(self.controller.component, text=self.text, style=self.style_name)
    self.place(relx=0.5, rely=0.5, anchor="w")

  def _configure_styles(self):
    style = ttk.Style()
    style.configure(self.style_name, foreground="#000000", background="#FFFFFF", font=("Helvetica", 12))

  def _bind_events(self):
    self.controller.component.bind('<Configure>', self._on_resize)

  def _on_resize(self, event):
    self.place_configure(relx=0.5, rely=0.5, anchor="w")