from ........shared.components.labelScaleSpinboxFrame.LabelScaleSpinboxFrame_Component import LabelScaleSpinboxFrameComponent
from ........shared.components.labelScaleSpinboxFrame.components.Scale_Component import ScaleComponent
from ........shared.components.labelScaleSpinboxFrame.components.Spinbox_Component import SpinBoxComponent
from ........shared.components.labelScaleSpinboxFrame.components.TextLabel_Component import TextLabelComponent

class ContrastFrameController:

  def __init__(self, parent):
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = LabelScaleSpinboxFrameComponent(self, relx=0.01, rely=0.1)

  def init_components(self):
    self.contrastTextLabel = TextLabelComponent(self, text="Contraste: ", style_name="ContrastLabel.TLabel")
    self.contrastSpinbox = SpinBoxComponent(self, command=self.on_spinbox_change)
    self.contrastScale = ScaleComponent(self, command=self.on_scale_move)

  def on_scale_move(self, value):
    self.contrastSpinbox.set_value(value)

  def on_spinbox_change(self, value):
    self.contrastScale.set_value(value)