from .HomeFrame_Component import HomeFrameComponent
from .components.TitleLabel_Component import TitleLabelComponent
from .frames.filesFrame.FilesFrame_Controller import FilesFrameController
from .frames.imageFrame.ImageFrame_Controller import ImageFrameController

class HomeFrameController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = HomeFrameComponent(self)

  def init_components(self):
    self.titleLabel = TitleLabelComponent(self)
    self.childrenControllers = {
        "FilesFrameController": FilesFrameController(self),
        "ImageFrameController": ImageFrameController(self),
      }
