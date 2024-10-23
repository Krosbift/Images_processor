from .Window_Tk import WindowTk
from .components.TitleLabel_Component import TitleLabelComponent
from .frames.filesSection.FilesFrame_Controller import FilesFrameController
from .frames.imageSection.ImageFrame_Controller import ImageFrameController

class WindowController:

  def __init__(self):
    self.childrenControllers = {}
    self.create_window()
    self.init_components()
    self.open_window()

  def create_window(self):
    self.windowTk = WindowTk(self)

  def init_components(self):
    self.titleLabel = TitleLabelComponent(self, self.windowTk)
    self.add_component("FilesFrameController", FilesFrameController(self))
    self.add_component("ImageFrameController", ImageFrameController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

  def open_window(self):
    self.windowTk.mainloop()

  def close_window(self):
    if self.windowTk is not None:
      self.windowTk.destroy()
      self.windowTk = None
