import sys
from load_image import ft_load
from zoom import get_zoomed
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def printShape(img:Image):
    img_array = np.array(img)
    print("Image shape (H, W, C):", img_array.shape)
    print("Pixel values (RGB):\n", img_array)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 test.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    img = ft_load(image_path)
    printShape(img)

    if img is not None:
        zoomed_img = get_zoomed(img, zoom_factor=2)
        if zoomed_img is not None:
            printShape(img)
            plt.imshow(zoomed_img)
            plt.title("Zoomed and Transposed Image")
            plt.xlabel("Pixels (X axis)")
            plt.ylabel("Pixels (Y axis)")
            plt.axis("on")
            plt.show()
