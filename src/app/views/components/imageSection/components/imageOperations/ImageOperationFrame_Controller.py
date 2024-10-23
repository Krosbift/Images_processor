from .ImageOperationFrame_Component import ImageOperationFrameComponent
from .components.brightnessSection.BrightnessFrame_Controller import BrightnessFrameController

class ImageOperationFrameController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = ImageOperationFrameComponent(self, self.parent_controller.component)

  def init_components(self):
    self.add_component('BrightnessFrameController', BrightnessFrameController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller
