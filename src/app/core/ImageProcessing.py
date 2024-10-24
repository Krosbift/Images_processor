import numpy as np
from PIL import Image
from scipy.ndimage import rotate

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
  

  def rotate_image(self, image, angle):
    """
    Rotate the image by a specified angle.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    angle (float): The angle by which to rotate the image, in degrees.
    
    Returns:
    PIL.Image.Image: The rotated image.
    """
    
    # Convert PIL Image to NumPy array
    image = np.array(image)
    
    # Ensure the angle is a float
    angle = float(angle)
    
    # Rotate the image
    rotated_image = rotate(image, angle, reshape=True, mode='nearest')
    
    # Convert back to PIL Image
    rotated_image = Image.fromarray(rotated_image.astype(np.uint8))
    
    return rotated_image


  def highlight_light_zones(self, image, threshold=200):
    """
    Highlight the light zones of an image.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    threshold (int): The threshold value to separate light zones.
    
    Returns:
    PIL.Image.Image: The image with light zones highlighted.
    """
    
    # Convert PIL Image to NumPy array
    image = np.array(image)
    
    # Create mask for light zones
    light_mask = image > threshold
    
    # Highlight light zones
    highlighted_image = np.zeros_like(image)
    highlighted_image[light_mask] = image[light_mask]
    
    # Convert back to PIL Image
    highlighted_image = Image.fromarray(highlighted_image)
    
    return highlighted_image


  def highlight_dark_zones(self, image, threshold=50):
    """
    Highlight the dark zones of an image.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    threshold (int): The threshold value to separate dark zones.
    
    Returns:
    PIL.Image.Image: The image with dark zones highlighted.
    """
    
    # Convert PIL Image to NumPy array
    image = np.array(image)
    
    # Create mask for dark zones
    dark_mask = image < threshold
    
    # Highlight dark zones
    highlighted_image = np.zeros_like(image)
    highlighted_image[dark_mask] = image[dark_mask]
    
    # Convert back to PIL Image
    highlighted_image = Image.fromarray(highlighted_image)
    
    return highlighted_image

