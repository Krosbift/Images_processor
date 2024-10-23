from .ImageFrame_Component import ImageFrameComponent
from .services.Image_Service import ImageService
from .components.imageLabel.ImageLabel_Controller import ImageLabelController

class ImageFrameController:

  def __init__(self, parent):
    self.service = ImageService()
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = ImageFrameComponent(self, self.parent_controller.windowTk)

  def init_components(self):
    self.add_component("ImageLabelController", ImageLabelController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

  def set_image(self):
    route = self.parent_controller.childrenControllers["FilesSectionController"].childrenControllers["FileEntryController"].path_route.get()
    width = self.component.winfo_width() * 0.7
    height = self.component.winfo_height()
    self.childrenControllers["ImageLabelController"].image = self.service.get_photo_image(route, width, height)
    self.childrenControllers["ImageLabelController"].component.update_image()