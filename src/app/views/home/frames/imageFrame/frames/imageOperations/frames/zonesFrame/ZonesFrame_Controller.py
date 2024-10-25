import threading
from tkinter import IntVar
from .ZonesFrame_Component import ZonesFrameComponent
from .components.ZonesNormalRadiobutton_Component import ZonesNormalRadiobuttonComponent
from .components.ZonesLightRadiobutton_Component import ZonesLightRadiobuttonComponent
from .components.ZonesDarkRadiobutton_Component import ZonesDarkRadiobuttonComponent


class ZonesFrameController:

  def __init__(self, parent):
    self.resize_timer = None
    self.value = IntVar(value=0)
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  
  def create_component(self):
    self.component = ZonesFrameComponent(self)
  

  def init_components(self):
    self.zones_normal_radiobutton = ZonesNormalRadiobuttonComponent(self)
    self.zones_light_radiobutton = ZonesLightRadiobuttonComponent(self)
    self.zones_dark_radiobutton = ZonesDarkRadiobuttonComponent(self)


  def toggle_state(self):
    if self.resize_timer is not None:
      self.resize_timer.cancel()
    self.resize_timer = threading.Timer(0.2, self.apply_image_zones, [self.value.get()])
    self.resize_timer.start()


  def apply_image_zones(self, value):
    if self.parent_controller.parent_controller.imageLabelComponent.original_image is not None:
      new_image = self.parent_controller.parent_controller.imageChangeService.set_zones(value)
      self.parent_controller.parent_controller.applied_image_operation(new_image)

