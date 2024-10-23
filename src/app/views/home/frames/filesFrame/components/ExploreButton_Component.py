from tkinter import ttk

class ExploreButtonComponent(ttk.Button):

  def __init__(self, controller):
    self.controller = controller
    self._configure_styles()
    self._configure_button()
    self._bind_events()

  def _configure_button(self):
    super().__init__(self.controller.component, text="Explorar", style="Explore.TButton", cursor="hand2", command=self.controller.get_file_path)
    self.place(relx=0.8, rely=0.5, relwidth=0.09, relheight=0.6, anchor="w")

  def _configure_styles(self):
    style = ttk.Style()
    style.configure("Explore.TButton", font=("Helvetica", 10), background="#E5E5E5", foreground="#111111", borderwidth=1)
    style.map("Explore.TButton", background=[('active', '#D5D5D5')], foreground=[('active', '#000000')])

  def _bind_events(self):
    self.controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(relx=0.8, rely=0.5, relwidth=0.09, relheight=0.6, anchor="w")
