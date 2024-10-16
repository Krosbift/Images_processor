from .Window_Tk import WindowTk
from .components.titleLabel.TitleLabel_Controller import TitleLabelController

class WindowController:
  window: WindowTk
  titleLabelController: TitleLabelController

  def __init__(self):
    self.create_window()
    self.init_components()
    self.open_window()

  def create_window(self):
    self.window = WindowTk()

  def init_components(self):
    self.titleLabelController = TitleLabelController(self.window)

  def open_window(self):
    self.window.mainloop()

  def close_window(self):
    if self.window is not None:
      self.window.destroy()
      self.window = None
