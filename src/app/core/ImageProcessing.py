import numpy as np
from PIL import Image

class ImageProcessing:

  def __init__(self):
    pass

  def adjust_brightness(self, image, factor):
    """
    Adjust the brightness of an image.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    factor (float): The factor by which to adjust the brightness. 
      Values > 1 will increase brightness, values < 1 will decrease it.
    
    Returns:
    PIL.Image.Image: The brightness-adjusted image.
    """

    # Convert PIL Image to NumPy array
    image = np.array(image)

    # Ensure the factor is a float
    factor = float(factor)
    
    # Adjust brightness
    adjusted_image = np.clip(image * factor, 0, 255).astype(np.uint8)
    
    # Convert back to PIL Image
    adjusted_image = Image.fromarray(adjusted_image)
    
    return adjusted_image


  def adjust_contrast(self, image, factor):
    """
    Adjust the contrast of an image.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    factor (float): The factor by which to adjust the contrast. 
      Values > 1 will increase contrast, values < 1 will decrease it.
    
    Returns:
    PIL.Image.Image: The contrast-adjusted image.
    """
    
    # Convert PIL Image to NumPy array
    image = np.array(image)
    
    # Ensure the factor is a float
    factor = float(factor)
    
    # Calculate the mean of the image
    mean = np.mean(image)
    
    # Adjust contrast
    adjusted_image = np.clip((image - mean) * factor + mean, 0, 255).astype(np.uint8)
    
    # Convert back to PIL Image
    adjusted_image = Image.fromarray(adjusted_image)
    
    return adjusted_image