from ...Window_Tk import WindowTk
from .TitleLabel_Component import TitleLabelComponent

class TitleLabelController:
  windowTk: WindowTk
  titleLabelComponent: TitleLabelComponent

  def __init__(self, window: WindowTk):
    self.windowTk = window
    self.create_component()

  def create_component(self):
    self.titleLabelComponent = TitleLabelComponent()

  def init_components(self):
    pass

  def destroy_component(self):
    pass
