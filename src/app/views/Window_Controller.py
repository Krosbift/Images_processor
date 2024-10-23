from .Window_Tk import WindowTk
from .home.HomeFrame_Controller import HomeFrameController

class WindowController:

  def __init__(self):
    self.create_window()
    self.init_components()
    self.open_window()

  def create_window(self):
    self.windowTk = WindowTk(self)

  def init_components(self):
    self.childrenControllers = {
        "HomeFrameController": HomeFrameController(self)
      }

  def open_window(self):
    self.windowTk.mainloop()
