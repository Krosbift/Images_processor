from .ImageOperationFrame_Component import ImageOperationFrameComponent
from .frames.brightnessFrame.BrightnessFrame_Controller import BrightnessFrameController
from .frames.contrastFrame.ContrastFrame_Controller import ContrastFrameController
from .frames.rotationFrame.RotationFrame_Controller import RotationFrameController
from .frames.zonesFrame.ZonesFrame_Controller import ZonesFrameController
from .frames.channelRGBFrame.ChannelRGBFrame_Controller import ChannelRGBFrameController
from .frames.channelCMYFrame.ChannelCMYFrame_Controller import ChannelCMYFrameController
from .frames.zoomFrame.ZoomFrame_Controller import ZoomFrameController
from .frames.binarizationFrame.BinarizationFrame_Controller import BinarizationFrameController
from .frames.negativeFrame.NegativeFrame_Controller import NegativeFrameController


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
        "ContrastFrameController": ContrastFrameController(self),
        "RotationFrameController": RotationFrameController(self),
        "ZonesFrameController": ZonesFrameController(self),
        "ChannelRGBFrameController": ChannelRGBFrameController(self),
        "ChannelCMYFrameController": ChannelCMYFrameController(self),
        "ZoomFrameController": ZoomFrameController(self),
        "BinarizationFrameController": BinarizationFrameController(self),
        "NegativeFrameController": NegativeFrameController(self),
      }

