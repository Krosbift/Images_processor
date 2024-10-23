from .TitleLabel_Component import TitleLabelComponent

class TitleLabelController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.titleLabelComponent = None
    self.childrenControllers = {}
    self.create_component()

  def create_component(self):
    self.titleLabelComponent = TitleLabelComponent(self, self.parent_controller.windowTk)

  def init_components(self):
    pass

  def destroy_component(self):
    pass
