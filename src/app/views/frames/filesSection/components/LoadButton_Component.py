import tkinter as tk

class LoadButtonComponent(tk.Button):

  def __init__(self, controller):
    self.controller = controller
    self._configure_button()
    self._bind_events()

  def _configure_button(self):
    super().__init__(
      self.controller.component,
      text="Cargar",
      font=("Helvetica", 10),
      bg="#E5E5E5",
      fg="#111111",
      bd=2,
      relief="solid",
      borderwidth=1,
      cursor="hand2",
      command=self.controller.set_image_path
    )
    self.place(relx=0.9, rely=0.5, relwidth=0.09, relheight=0.5, anchor="w")

  def _bind_events(self):
    self.controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.9, rely=0.5, relwidth=0.09, relheight=0.5, anchor="w")