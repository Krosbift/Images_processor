from tkinter import ttk, StringVar

class SpinBoxComponent(ttk.Spinbox):

  def __init__(self, controller, command):
    self.controller = controller
    self.command = command
    self._configure_spinbox()
    self._configure_styles()
    self._bind_events()
    self.set(0)

  def _configure_spinbox(self):
    super().__init__(self.controller.component, from_=0, to=2, increment=0.01, style="TSpinbox", state="readonly", command=self._on_spinbox_change)
    self.place(relx=0.68, rely=0.5, relwidth=0.13, relheight=0.6, anchor="w")

  def _configure_styles(self):
    style = ttk.Style()
    style.configure("TSpinbox", arrowsize=20)
    style.layout("TSpinbox", [
      ("Spinbox.field", {"children": [
      ("Spinbox.padding", {"children": [
        ("Spinbox.textarea", {"sticky": "nswe"}),
        ("Spinbox.uparrow", {"side": "right", "sticky": "ns"}),
        ("Spinbox.downarrow", {"side": "right", "sticky": "ns"})
      ], "sticky": "nswe"})
      ], "sticky": "nswe"})
    ])
    style.map("TSpinbox", fieldbackground=[('readonly', 'white')], selectbackground=[('readonly', 'white')], selectforeground=[('readonly', 'black')])

  def _bind_events(self):
    self.controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.68, rely=0.5, relwidth=0.13, relheight=0.6, anchor="w")

  def _on_spinbox_change(self):
    self.command(self.get())

  def set_value(self, value):
    self.set(f"{float(value):.2f}")
