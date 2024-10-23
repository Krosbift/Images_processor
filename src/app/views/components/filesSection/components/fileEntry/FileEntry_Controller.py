from .FileEntry_Component import FileEntryComponent

class FileEntryController:

  def __init__(self, parent) -> None:
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = FileEntryComponent(self, self.parent_controller.component)

  def init_components(self):
    pass

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

  def destroy_component(self):
    pass
