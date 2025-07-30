import numpy as np
from load_image import ft_load, printShape
import matplotlib.pyplot as plt


def get_zoomed(img_array: np.ndarray, zoom_factor=2):
    "return zoomed img object"
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

        return cropped

    except Exception as e:
        print(f"Error displaying image: {e}")


if __name__ == "__main__":
    img = ft_load("animal.jpeg")

    if img is not None:
        zoomed = get_zoomed(img, zoom_factor=2)
        printShape(zoomed)
        if zoomed is not None:
            plt.imshow(zoomed)
            plt.title("Zoomed and Transposed Image")
            plt.xlabel("Pixels (X axis)")
            plt.ylabel("Pixels (Y axis)")
            plt.axis("on")
            plt.show()
