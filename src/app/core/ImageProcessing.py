import numpy as np
from PIL import Image, ImageTk

class ImageProcessing:
  def __init__(self):
    pass

  def adjust_brightness(self, image_path, factor):
    """
    Adjust the brightness of an image.
    
    Parameters:
    image_path (str): The path to the input image.
    factor (float): The factor by which to adjust the brightness. 
      Values > 1 will increase brightness, values < 1 will decrease it.
    
    Returns:
    ImageTk.PhotoImage: The brightness-adjusted image suitable for tkinter.
    """
    # Load the image
    image = Image.open(image_path)
    image = np.array(image)

    # Ensure the factor is a float
    factor = float(factor)
    
    # Adjust brightness
    adjusted_image = np.clip(image * factor, 0, 255).astype(np.uint8)
    
    # Convert back to PIL Image
    adjusted_image = Image.fromarray(adjusted_image)
    
    # Convert to ImageTk.PhotoImage
    tk_image = ImageTk.PhotoImage(adjusted_image)
    
    return tk_image
