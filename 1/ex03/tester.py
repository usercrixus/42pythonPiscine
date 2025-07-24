import sys
from load_image import ft_load
from zoom import get_zoomed
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 transpose_image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    img = ft_load(image_path)

    if img is not None:
        zoomed_img = get_zoomed(img, zoom_factor=2)
        if zoomed_img is not None:
            plt.imshow(zoomed_img)
            plt.title("Zoomed and Transposed Image")
            plt.xlabel("Pixels (X axis)")
            plt.ylabel("Pixels (Y axis)")
            plt.axis("on")
            plt.show()
