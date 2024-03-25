from PIL import Image, ImageEnhance, ImageDraw, ImageFont
# import numpy as np  # Import NumPy for advanced image processing


def open_and_convert_image(image_path):
  """Opens an image and converts it to a compatible mode (RGB or RGBA)."""


  try:
    img = Image.open(image_path)
    format = img.format
    if format in ("JPEG", "JPG"):
      img = img.convert('RGB')
    elif format == "PNG":
      img = img.convert('RGBA')
    else:
      img = img.convert('P')  # Grayscale or other formats (optional conversion)
    return img
  except Exception as e:
    print(f"Error opening image: {e}")
    return None  # Indicate error


def edit_image(img, output_path, edit_type, edit_amount=1):
  """Edits an image based on the specified type and amount (assuming img is already opened and converted)."""

  try:

    if edit_type == "brightness":
      editor = ImageEnhance.Brightness(img)
      edited_img = editor.enhance(edit_amount)
    elif edit_type == "contrast":
      editor = ImageEnhance.Contrast(img)
      edited_img = editor.enhance(edit_amount)

    edited_img.save(output_path)
    print(f"Image edited and saved to {output_path}.")

  except Exception as e:
    print(f"Error editing image: {e}")

def edit_any_image(image_path, output_path, edit_type, edit_amount=1):
  """Attempts to edit images of any supported format using Pillow."""

  try:
    # Open and convert the image
    img = open_and_convert_image(image_path)
    if img is None: # if no image found
        print("Error: Could not open the image file.")
        return  # Handle error from open_and_convert_image

    # Delegate editing to the original function
    edit_image(img, output_path, edit_type, edit_amount)

  except Exception as e:
    print(f"Error editing image: {e}")

# image_path = ""  # path of image file tobe edited
# output_path = "" # after editing save 

image_path = "ImageProcessor/imgs/Image.jpg"  # change Image.jpg with your real image name
output_path = "ImageProcessor/Edited Imgs/edited_image.jpg"


edit_any_image(image_path, output_path, "contrast", 1.2)



