import threading
from .ZoomFrame_Component import ZoomFrameComponent
from .components.ZoomLabel_Component import ZoomLabelComponent
from .components.ZoomRefLabel_Component import ZoomRefLabelComponent
from .components.ZoomSpinbox_component import ZoomSpinboxComponent


class ZoomFrameController:

  def __init__(self, parent) -> None:
    self.resize_timer = None
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  
  def create_component(self):
    self.component = ZoomFrameComponent(self)


  def init_components(self):
    self.zoom_label_component = ZoomLabelComponent(self)
    self.zoom_label_x_component = ZoomRefLabelComponent(self, relx=0.37, rely=0.05, text="X Value: ")
    self.zoom_label_y_component = ZoomRefLabelComponent(self, relx=0.37, rely=0.42, text="Y Value: ")
    self.zoom_label_factor_component = ZoomRefLabelComponent(self, relx=0.37, rely=0.72, text="Factor: ")
    self.zoom_spinbox_x_component = ZoomSpinboxComponent(self, relx=0.5, rely=0.05, min_value=0, max_value=2000, command=self.new_values, initial_value=0, increment=1)
    self.zoom_spinbox_y_component = ZoomSpinboxComponent(self, relx=0.5, rely=0.42, min_value=0, max_value=2000, command=self.new_values, initial_value=0, increment=1)
    self.zoom_spinbox_factor_component = ZoomSpinboxComponent(self, relx=0.5, rely=0.72, min_value=0, max_value=10, command=self.new_values, initial_value=1, increment=0.1)


  def new_values(self):
    if self.resize_timer is not None:
      self.resize_timer.cancel()
    self.resize_timer = threading.Timer(1, self.update_zoom_image, [float(self.zoom_spinbox_x_component.get()), float(self.zoom_spinbox_y_component.get()), float(self.zoom_spinbox_factor_component.get())])
    self.resize_timer.start()

  
  def update_zoom_image(self, x, y, factor):
    if self.parent_controller.parent_controller.imageLabelComponent.original_image is not None:
      new_image = self.parent_controller.parent_controller.imageChangeService.set_zoom(x, y, factor)
      self.parent_controller.parent_controller.applied_image_operation(new_image)
