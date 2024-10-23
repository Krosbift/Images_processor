from ........shared.components.labelScaleSpinboxFrame.LabelScaleSpinboxFrame_Component import LabelScaleSpinboxFrameComponent
from ........shared.components.labelScaleSpinboxFrame.components.Scale_Component import ScaleComponent
from ........shared.components.labelScaleSpinboxFrame.components.Spinbox_Component import SpinBoxComponent
from ........shared.components.labelScaleSpinboxFrame.components.TextLabel_Component import TextLabelComponent

class BrightnessFrameController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = LabelScaleSpinboxFrameComponent(self, relx=0.01, rely=0.005)

  def init_components(self):
    self.brightnessTextLabel = TextLabelComponent(self, text="Brillo: ", style_name="BrightnessLabel.TLabel")
    self.brightnessSpinbox = SpinBoxComponent(self)
    self.brightnessScale = ScaleComponent(self, command=self.on_scale_move)

  def on_scale_move(self, value):
    self.brightnessSpinbox.set_value(value)
