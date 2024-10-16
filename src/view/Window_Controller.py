from .Window_Tk import WindowTk
from .components.titleLabel.TitleLabel_Controller import TitleLabelController

class WindowController:
  windowTk: WindowTk
  titleLabelController: TitleLabelController

  def __init__(self):
    self.create_window()
    self.init_components()
    self.open_window()

  def create_window(self):
    self.windowTk = WindowTk(self)

  def init_components(self):
    self.titleLabelController = TitleLabelController(self.WindowTk)

  def open_window(self):
    self.windowTk.mainloop()

  def close_window(self):
    if self.windowTk is not None:
      self.windowTk.destroy()
      self.windowTk = None
