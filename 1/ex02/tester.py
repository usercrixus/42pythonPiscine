import sys
from load_image import ft_load
from PIL import Image # pip install pillow
import numpy as np # pip install numpy

def printShape(img:Image):
    img_array = np.array(img)
    print("Image shape (H, W, C):", img_array.shape)
    print("Pixel values (RGB):\n", img_array)

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 load_image.py <image_path>")
        sys.exit(1)
    else:
        img = ft_load(argv[1])
        printShape(img)
