from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  # pip install matplotlib
from load_image import ft_load

def get_zoomed(img:Image, zoom_factor=2):
    img_array = np.array(img)
    try:
        if img_array is None:
            raise ValueError("No image data to display.")

        # Get dimensions
        h, w, channel = img_array.shape

        # Compute zoomed region (center crop zoom)
        zh, zw = h // zoom_factor, w // zoom_factor
        top = (h - zh) // 2
        left = (w - zw) // 2
        cropped = img_array[top:top+zh, left:left+zw]

        return Image.fromarray(cropped).resize((w, h), Image.NEAREST)

    except Exception as e:
        print(f"Error displaying image: {e}")
