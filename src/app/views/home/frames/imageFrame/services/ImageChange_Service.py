from PIL import Image, ImageTk
from ......core.ImageProcessing import ImageProcessing


class ImageChangeService:


  def __init__(self) -> None:
    self.imageProcessing = ImageProcessing()
    self.image = None
    self.brightness = 1
    self.contrast = 1
    self.rotation = 0
    self.zones = 0
    self.type = None
    self.channelRGB = None
    self.channelCNY = None
    self.transparence = None
    self.binarity = None
    self.negative = None


  def apply_filter(self):
    if self.image is not None:
      image = self.image
      image = self.imageProcessing.adjust_brightness(image, self.brightness)
      image = self.imageProcessing.adjust_contrast(image, self.contrast)
      image = self.imageProcessing.rotate_image(image, self.rotation)
      image = (
          image if self.zones == 0 else self.imageProcessing.highlight_light_zones(image) 
          if self.zones == 1 else self.imageProcessing.highlight_dark_zones(image)
        )
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
  

  def set_rotation(self, value):
    self.rotation = value
    return self.apply_filter()
  
  def set_zones(self, value):
    self.zones = value
    return self.apply_filter()

