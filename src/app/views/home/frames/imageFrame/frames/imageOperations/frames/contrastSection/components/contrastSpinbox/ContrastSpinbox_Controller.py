from .ContrastSpinbox_Component import ContrastSpinBoxComponent

class ContrastSpinBoxController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.component = None
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = ContrastSpinBoxComponent(self, self.parent_controller.component)

  def init_components(self):
    pass

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

  def set_value(self, value):
    formatted_value = f"{float(value):.2f}"
    self.component.set(formatted_value)
