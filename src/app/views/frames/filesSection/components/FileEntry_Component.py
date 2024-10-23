import tkinter as tk

class FileEntryComponent(tk.Entry):

  def __init__(self, controller):
    self.path_route = tk.StringVar()
    self.controller = controller
    self._configure_button()
    self._bind_events()

  def _configure_button(self):
    super().__init__(
      self.controller.component,
      font=("Helvetica", 10),
      bg="#FFFFFF",
      fg="#111111",
      bd=2,
      relief="solid",
      borderwidth=1,
      state="readonly",
      textvariable=self.path_route
    )
    self.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="center")

  def _bind_events(self):
    self.controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="center")

  def set_textvariable(self, new_value):
    self.path_route.set(new_value)
