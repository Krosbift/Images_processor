from tkinter import ttk

class BrightnessSpinBoxComponent(ttk.Spinbox):
  
  def __init__(self, controller, section):
    self.controller = controller
    self.section = section
    self.init_config()
    self.section.bind("<Configure>", self.on_resize)
    self.set(0)

  def init_config(self):
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
    style.map("TSpinbox", 
          fieldbackground=[('readonly', 'white')],
          selectbackground=[('readonly', 'white')],
          selectforeground=[('readonly', 'black')])

    super().__init__(self.section, from_=0, to=1, increment=0.01, style="TSpinbox", state="readonly")
    self.place(relx=0.68, rely=0.5, relwidth=0.13, relheight=0.6, anchor="w")

  def on_resize(self, _):
    self.place_configure(relx=0.68, rely=0.5, relwidth=0.13, relheight=0.6, anchor="w")
