import tkinter as tk
import threading

class ImageLabelComponent(tk.Label):
  
  def __init__(self, controller):
    self.image = None
    self.controller = controller
    self._configure_label()
    self._bind_events()
    self.resize_timer = None

  def _configure_label(self):
    super().__init__(self.controller.component, highlightthickness=1)
    self.place(x=0, y=0, relwidth=0.7, relheight=1, anchor="nw")

  def _bind_events(self):
    self.controller.parent_controller.component.bind("<Configure>", self._on_resize)

  def _on_resize(self, _):
    self.place_configure(x=0, y=0, relwidth=0.7, relheight=1, anchor="nw")
    if self.resize_timer is not None:
      self.resize_timer.cancel()
    self.resize_timer = threading.Timer(0.2, self._resize_image)
    self.resize_timer.start()

  def _resize_image(self):
    if self.controller.parent_controller.childrenControllers["FilesFrameController"].fileEntryComponent.path_route.get() != "":
      self.update_image()

  def update_image(self):
    self.image = self.controller.service.get_photo_image(
        self.controller.parent_controller.childrenControllers["FilesFrameController"].fileEntryComponent.path_route.get(),
        self.controller.component.winfo_width() * 0.7,
        self.controller.component.winfo_height()
      )
    self.config(image=self.image)
    self.update()
