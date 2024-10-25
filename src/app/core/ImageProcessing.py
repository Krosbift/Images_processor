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


  def apply_rgb_filter(self, image, show_red, show_green, show_blue):
    """
    Apply an RGB filter to an image by showing or hiding specific channels.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    show_red (bool): Whether to show the red channel.
    show_green (bool): Whether to show the green channel.
    show_blue (bool): Whether to show the blue channel.
    
    Returns:
    PIL.Image.Image: The RGB-filtered image.
    """
    image = np.array(image)
    
    red_mask = np.zeros_like(image)
    green_mask = np.zeros_like(image)
    blue_mask = np.zeros_like(image)
    
    if show_red:
        red_mask[:, :, 0] = image[:, :, 0]
    if show_green:
        green_mask[:, :, 1] = image[:, :, 1]
    if show_blue:
        blue_mask[:, :, 2] = image[:, :, 2]
    
    filtered_rgb_image = red_mask + green_mask + blue_mask
    
    if show_red and not show_green and not show_blue:
        filtered_rgb_image[:, :, 1] = 0
        filtered_rgb_image[:, :, 2] = 0
    elif show_green and not show_red and not show_blue:
        filtered_rgb_image[:, :, 0] = 0
        filtered_rgb_image[:, :, 2] = 0
    elif show_blue and not show_red and not show_green:
        filtered_rgb_image[:, :, 0] = 0
        filtered_rgb_image[:, :, 1] = 0
    
    filtered_image = Image.fromarray(filtered_rgb_image.astype(np.uint8))
    
    return filtered_image


  def apply_cmy_filter(self, image, show_cyan, show_magenta, show_yellow):
    """
    Apply a CMY filter to an image by showing or hiding specific channels.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    show_cyan (bool): Whether to show the cyan channel.
    show_magenta (bool): Whether to show the magenta channel.
    show_yellow (bool): Whether to show the yellow channel.
    
    Returns:
    PIL.Image.Image: The CMY-filtered image.
    """
    image = np.array(image)
    
    cmy_image = 255 - image
    
    cyan_mask = np.zeros_like(cmy_image)
    magenta_mask = np.zeros_like(cmy_image)
    yellow_mask = np.zeros_like(cmy_image)
    
    if show_cyan:
        cyan_mask[:, :, 0] = cmy_image[:, :, 0]
    if show_magenta:
        magenta_mask[:, :, 1] = cmy_image[:, :, 1]
    if show_yellow:
        yellow_mask[:, :, 2] = cmy_image[:, :, 2]
    
    filtered_cmy_image = cyan_mask + magenta_mask + yellow_mask
    
    if show_cyan and not show_magenta and not show_yellow:
        filtered_cmy_image[:, :, 1] = 0
        filtered_cmy_image[:, :, 2] = 0
    elif show_magenta and not show_cyan and not show_yellow:
        filtered_cmy_image[:, :, 0] = 0
        filtered_cmy_image[:, :, 2] = 0
    elif show_yellow and not show_cyan and not show_magenta:
        filtered_cmy_image[:, :, 0] = 0
        filtered_cmy_image[:, :, 1] = 0
    
    rgb_image = 255 - filtered_cmy_image
    
    filtered_image = Image.fromarray(rgb_image.astype(np.uint8))
    
    return filtered_image


  def zoom_image(self, image, x, y, scale_factor):
    """
    Zoom into an image from a specified point (x, y) with a given scale factor.
    
    Parameters:
    image (PIL.Image.Image): The input image.
    x (int): The x-coordinate of the initial point.
    y (int): The y-coordinate of the initial point.
    scale_factor (float): The scale factor for zooming.
    
    Returns:
    PIL.Image.Image: The zoomed image.
    """
    if scale_factor == 1 or scale_factor == 1.0 or scale_factor == 0:
        return image

    image = np.array(image)
    height, width = image.shape[:2]
    new_height, new_width = int(height / scale_factor), int(width / scale_factor)
    
    # Calculate the cropping box
    left = int(max(0, x - new_width // 2))
    right = int(min(width, x + new_width // 2))
    top = int(max(0, y - new_height // 2))
    bottom = int(min(height, y + new_height // 2))
    
    # Crop the image
    cropped_image = image[top:bottom, left:right]
    
    # Resize the cropped image to the original dimensions
    zoomed_image = np.array(Image.fromarray(cropped_image).resize((width, height), Image.LANCZOS))
    
    return Image.fromarray(zoomed_image)

