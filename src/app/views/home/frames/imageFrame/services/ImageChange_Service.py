from PIL import Image
from ......core.ImageProcessing import ImageProcessing


class ImageChangeService:

  def __init__(self) -> None:
    self.imageProcessing = ImageProcessing()
    self.image = None
    self.brightness = 1
    self.contrast = 1
    self.rotation = 0
    self.zones = 0
    self.channelR = 1
    self.channelG = 1
    self.channelB = 1
    self.channelC = 1
    self.channelN = 1
    self.channelY = 1
    self.zoomX = 0
    self.zoomY = 0
    self.zoomFactor = 1
    self.type = None
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
      image = self.imageProcessing.apply_rgb_filter(image, self.channelR, self.channelG, self.channelB)
      image = self.imageProcessing.apply_cmy_filter(image, self.channelC, self.channelN, self.channelY)
      image = self.imageProcessing.zoom_image(image, self.zoomX, self.zoomY, self.zoomFactor)
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


  def set_rgb_filter(self, valueR, valueG, valueB):
    self.channelR = valueR
    self.channelG = valueG
    self.channelB = valueB
    return self.apply_filter()


  def set_cmy_filter(self, valueC, valueM, valueY):
    self.channelC = valueC
    self.channelN = valueM
    self.channelY = valueY
    return self.apply_filter()


  def set_zoom(self, valueX, valueY, factor):
    self.zoomX = valueX
    self.zoomY = valueY
    self.zoomFactor = factor
    return self.apply_filter()


  def get_widthxheight(self):
    if self.image is not None:
      return self.image.size
    return 0, 0

