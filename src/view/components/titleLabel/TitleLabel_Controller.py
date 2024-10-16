from .TitleLabel_Component import TitleLabelComponent

class TitleLabelController:
  titleLabelComponent: TitleLabelComponent

  def __init__(self, window):
    self.window = window
    self.create_component()

  def create_component(self):
    self.titleLabelComponent = TitleLabelComponent(self.window)

  def init_components(self):
    pass

  def destroy_component(self):
    pass
