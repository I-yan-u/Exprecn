from PIL import Image, ImageOps
from io import BytesIO
from typing import Tuple

def resize_image(image: bytes) -> bytes:
    """Resizes the image"""
    size = (240, 240)
    # Resize the image to 240x240
    new_image = ImageOps.contain(image, size)

    return new_image

def process_image(image_data: bytes) -> Tuple[bytes, int]:
    """Uploads image data"""
    # with open(image_data, 'rb') as image_file:
    #     image_data = image_file.read()

    # Create a BytesIO object to read image data
    image_stream = BytesIO(image_data.read())
    
    # Open the image using PIL
    image = Image.open(image_stream)

    # Resize the image
    image = resize_image(image)

    # Convert the image back to binary data
    image_buffer = BytesIO()
    image.save(image_buffer, format='PNG')  # Adjust the format as per your needs
    image_binary = image_buffer.getvalue()
    return image_binary, len(image_binary)