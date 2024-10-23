from .ContrastFrame_Component import ContrastFrameComponent
from .components.contrastTextLabel.ContrastTextLabel_Controller import ContrastTextLabelController
from .components.contrastSpinbox.ContrastSpinbox_Controller import ContrastSpinBoxController
from .components.contrastScale.ContrastScale_Controller import ContrastScaleController

class ContrastFrameController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = ContrastFrameComponent(self, self.parent_controller.component)

  def init_components(self):
    self.add_component("ContrastTextLabelController", ContrastTextLabelController(self))
    self.add_component("ContrastSpinBoxController", ContrastSpinBoxController(self))
    self.add_component("ContrastScaleController", ContrastScaleController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller
