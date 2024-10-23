from .services.Image_Service import ImageService
from .ImageFrame_Component import ImageFrameComponent
from .components.ImageLabel_Component import ImageLabelComponent
from .frames.imageOperations.ImageOperationFrame_Controller import ImageOperationFrameController

class ImageFrameController:

  def __init__(self, parent):
    self.service = ImageService()
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = ImageFrameComponent(self)

  def init_components(self):
    self.imageLabelComponent = ImageLabelComponent(self)
    self.childrenControllers = {
        "ImageOperationFrameController": ImageOperationFrameController(self)
      }

  def set_image(self):
    self.imageLabelComponent.update_image()
