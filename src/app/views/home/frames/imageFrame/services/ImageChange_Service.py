from PIL import Image, ImageTk
from ......core.ImageProcessing import ImageProcessing


class ImageChangeService:


  def __init__(self) -> None:
    self.imageProcessing = ImageProcessing()
    self.image = None
    self.brightness = 1
    self.contrast = 1
    self.zones = None
    self.type = None
    self.channelRGB = None
    self.channelCNY = None
    self.rotation = None
    self.transparence = None
    self.binarity = None
    self.negative = None


  def apply_filter(self):
    if self.image is not None:
      image = self.image
      image = self.imageProcessing.adjust_brightness(image, self.brightness)
      image = self.imageProcessing.adjust_contrast(image, self.contrast)
      return image


  def set_image(self, route):
    self.image = Image.open(route)
    return self.apply_filter()


  def set_brightness(self, value):
    self.brightness = value
    return self.apply_filter()


  def set_contrast(self, value):
    self.contrast = value
    return self.apply_filter()