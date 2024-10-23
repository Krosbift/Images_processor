import tkinter as tk
from tkinter import ttk

class FileEntryComponent(ttk.Entry):

  def __init__(self, controller):
    self.path_route = tk.StringVar(value="")
    self.controller = controller
    self._configure_styles()
    self._configure_entry()
    self._bind_events()

  def _configure_entry(self):
    super().__init__(self.controller.component, font=("Helvetica", 10), textvariable=self.path_route, style="FileEntry.TEntry", state="readonly")
    self.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.6, anchor="center")

  def _configure_styles(self):
    style = ttk.Style()
    style.configure("FileEntry.TEntry", font=("Helvetica", 10), foreground="black", background="lightgray", padding=2, bordercolor="black", relief="solid", borderwidth=1)
    style.map("FileEntry.TEntry", fieldbackground=[('readonly', 'lightgray')], foreground=[('readonly', 'black')])

  def _bind_events(self):
    self.controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.6, anchor="center")

  def set_textvariable(self, new_value):
    self.path_route.set(new_value)
