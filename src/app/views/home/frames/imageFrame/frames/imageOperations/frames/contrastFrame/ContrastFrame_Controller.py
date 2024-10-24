import threading
from ........shared.components.labelScaleSpinboxFrame.LabelScaleSpinboxFrame_Component import LabelScaleSpinboxFrameComponent
from ........shared.components.labelScaleSpinboxFrame.components.Scale_Component import ScaleComponent
from ........shared.components.labelScaleSpinboxFrame.components.Spinbox_Component import SpinBoxComponent
from ........shared.components.labelScaleSpinboxFrame.components.TextLabel_Component import TextLabelComponent

class ContrastFrameController:


  def __init__(self, parent):
    self.resize_timer = None
    self.parent_controller = parent
    self.create_component()
    self.init_components()


  def create_component(self):
    self.component = LabelScaleSpinboxFrameComponent(self, relx=0.01, rely=0.1)


  def init_components(self):
    self.contrastTextLabel = TextLabelComponent(self, text="Contraste: ", style_name="ContrastLabel.TLabel")
    self.contrastSpinbox = SpinBoxComponent(self, command=self.on_spinbox_change, initial_value=1, min_value=0, max_value=2, increment=0.01, notation="float_2_decimals")
    self.contrastScale = ScaleComponent(self, command=self.on_scale_move, initial_value=1, min_value=0, max_value=2)


  def on_scale_move(self, value):
    self.contrastSpinbox.set_value(value)
    if self.resize_timer is not None:
      self.resize_timer.cancel()
    self.resize_timer = threading.Timer(0.2, self.apply_image_contrast, [value])
    self.resize_timer.start()


  def on_spinbox_change(self, value):
    self.contrastScale.set_value(value)
    if self.resize_timer is not None:
      self.resize_timer.cancel()
    self.resize_timer = threading.Timer(0.2, self.apply_image_contrast, [value])
    self.resize_timer.start()


  def apply_image_contrast(self, value):
    if self.parent_controller.parent_controller.imageLabelComponent.original_image is not None:
      new_image = self.parent_controller.parent_controller.imageChangeService.set_contrast(value)
      self.parent_controller.parent_controller.applied_image_operation(new_image)