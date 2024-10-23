from .services.File_Service import FileService
from .FilesFrame_Component import FilesFrameComponent
from .components.FileLabel_Component import FileLabelComponent
from .components.FileEntry_Component import FileEntryComponent
from .components.ExploreButton_Component import ExploreButtonComponent
from .components.LoadButton_Component import LoadButtonComponent

class FilesFrameController:

  def __init__(self, parent):
    self.service = FileService()
    self.parent_controller = parent
    self.create_component()
    self.init_components()

  def create_component(self):
    self.component = FilesFrameComponent(self)

  def init_components(self):
    self.loadButtonComponent = LoadButtonComponent(self)
    self.exploreButtonComponent = ExploreButtonComponent(self)
    self.fileEntryComponent = FileEntryComponent(self)
    self.fileLabelComponent = FileLabelComponent(self)

  def get_file_path(self):
    self.fileEntryComponent.set_textvariable(self.service.select_file())

  def set_image_path(self):
    return self.parent_controller.childrenControllers["ImageFrameController"].set_image()
