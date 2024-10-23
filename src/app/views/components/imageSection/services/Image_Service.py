from PIL import Image, ImageTk

class ImageService:

  def __init__(self) -> None:
    pass

  def get_photo_image(self, route, width, height):
    image = Image.open(route)
    image = image.resize((int(width), int(height)), Image.LANCZOS)
    return ImageTk.PhotoImage(image)