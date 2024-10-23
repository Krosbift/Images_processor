from .BrightnessFrame_Component import BrightnessFrameComponent
from .components.brightnessTextLabel.BrightnessTextLabel_Controller import BrightnessTextLabelController
from .components.brightnessSpinbox.BrightnessSpinBox_Controller import BrightnessSpinBoxController
from .components.brightnessScale.BrightnessScale_Controller import BrightnessScaleController

class BrightnessFrameController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = BrightnessFrameComponent(self, self.parent_controller.component)

  def init_components(self):
    self.add_component('BrightnessTextLabelController', BrightnessTextLabelController(self))
    self.add_component('BrightnessSpinBoxController', BrightnessSpinBoxController(self))
    self.add_component('BrightnessScaleController', BrightnessScaleController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller
