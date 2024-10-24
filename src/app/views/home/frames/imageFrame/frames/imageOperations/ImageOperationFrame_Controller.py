from .ImageOperationFrame_Component import ImageOperationFrameComponent
from .frames.brightnessFrame.BrightnessFrame_Controller import BrightnessFrameController
from .frames.contrastFrame.ContrastFrame_Controller import ContrastFrameController


class ImageOperationFrameController:


  def __init__(self, parent):
    self.parent_controller = parent
    self.component = None
    self.create_component()
    self.init_components()


  def create_component(self):
    self.component = ImageOperationFrameComponent(self)


  def init_components(self):
    self.childrenControllers = {
        "BrightnessFrameController": BrightnessFrameController(self),
        "ContrastFrameController": ContrastFrameController(self)
      }

