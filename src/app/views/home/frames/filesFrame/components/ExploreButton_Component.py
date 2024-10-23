from .....shared.components.ButtonStandard_Component import ButtonStandardComponent

class ExploreButtonComponent(ButtonStandardComponent):
  
  def __init__(self, controller):
    super().__init__(controller, text="Explorar", style="Explore.TButton", command=controller.get_file_path, relx=0.8)