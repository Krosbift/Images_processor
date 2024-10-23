from .LoadButton_Component import LoadButtonComponent

class LoadButtonController:

  def __init__(self, parent) -> None:
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = LoadButtonComponent(self, self.parent_controller.component)

  def init_components(self):
    pass

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

