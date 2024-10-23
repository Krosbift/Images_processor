from .....shared.components.ButtonStandard_Component import ButtonStandardComponent

class LoadButtonComponent(ButtonStandardComponent):
  
  def __init__(self, controller):
    self.controller = controller
    super().__init__(self.controller, text="Cargar", style="Load.TButton", command=self.controller.set_image_path, relx=0.9)