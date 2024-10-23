from .Window_Tk import WindowTk
from .components.titleLabel.TitleLabel_Controller import TitleLabelController
from .components.filesSection.FilesSection_Controller import FilesSectionController

class WindowController:

  def __init__(self):
    self.windowTk = None
    self.childrenControllers = {}
    self.create_window()
    self.init_components()
    self.open_window()

  def create_window(self):
    self.windowTk = WindowTk(self)

  def init_components(self):
    self.add_component("TitleLabelController", TitleLabelController(self))
    self.add_component("FilesSectionController", FilesSectionController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

  def remove_component(self, key):
    self.childrenControllers.pop(key)

  def open_window(self):
    self.windowTk.mainloop()

  def close_window(self):
    if self.windowTk is not None:
      self.windowTk.destroy()
      self.windowTk = None
