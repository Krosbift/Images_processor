from .services.Image_Service import ImageService
from .services.ImageChange_Service import ImageChangeService
from .ImageFrame_Component import ImageFrameComponent
from .components.ImageLabel_Component import ImageLabelComponent
from .frames.imageOperations.ImageOperationFrame_Controller import ImageOperationFrameController


class ImageFrameController:
  """
  ImageFrameController is responsible for managing the image frame component and its interactions.
  Attributes:
    service (ImageService): Service for handling image-related operations.
    imageChangeService (ImageChangeService): Service for handling image change operations.
    parent_controller: Reference to the parent controller.
    component (ImageFrameComponent): The image frame component managed by this controller.
    imageLabelComponent (ImageLabelComponent): Component for displaying and managing the image label.
    childrenControllers (dict): Dictionary of child controllers.
  Methods:
    __init__(parent): Initializes the ImageFrameController with a parent controller.
    create_component(): Creates the image frame component.
    init_components(): Initializes the components used by the controller.
    init_childControllers(): Initializes the child controllers.
    set_image(): Loads the image into the image label component.
    applied_image_operation(image): Updates the image label component with the given image.
  """

  def __init__(self, parent):
    self.service = ImageService()
    self.imageChangeService = ImageChangeService()
    self.parent_controller = parent
    self.create_component()
    self.init_components()


  def create_component(self):
    self.component = ImageFrameComponent(self)


  def init_components(self):
    self.imageLabelComponent = ImageLabelComponent(self)


  def init_childControllers(self):
    self.childrenControllers = {
        "ImageOperationFrameController": ImageOperationFrameController(self)
    }


  def set_image(self):
    self.imageLabelComponent.load_image()


  def applied_image_operation(self, image):
    self.imageLabelComponent.update_image(image)

