from .services.File_Service import FileService
from .FilesFrame_Component import FilesFrameComponent
from .components.fileLabel.FileLabel_Controller import FileLabelController
from .components.loadButton.LoadButton_Controller import LoadButtonController
from .components.exploreButton.ExploreButton_Controller import ExploreButtonController
from .components.fileEntry.FileEntry_Controller import FileEntryController

class FilesSectionController:

  def __init__(self, parent):
    self.service = FileService()
    self.parent_controller = parent
    self.component = None
    self.childrenControllers = {}
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = FilesFrameComponent(self, self.parent_controller.windowTk)

  def init_components(self):
    self.add_component("LoadButtonController", LoadButtonController(self))
    self.add_component("ExploreButtonController", ExploreButtonController(self))
    self.add_component("FileEntryController", FileEntryController(self))
    self.add_component("FileLabelController", FileLabelController(self))

  def add_component(self, key, controller):
    self.childrenControllers[key] = controller

  def destroy_component(self):
    pass

  def get_file_path(self):
    self.childrenControllers["FileEntryController"].component.path_route.set(self.service.select_file())
