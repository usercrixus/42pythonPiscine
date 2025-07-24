import sys
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image # pip install pillow
from pimp_image import *

def printShape(img:Image):
    img_array = np.array(img)
    print("Image shape (H, W, C):", img_array.shape)
    print("Pixel values (RGB):\n", img_array)

def print_img(img:Image):
    img_array = np.array(img)
    plt.imshow(img_array)
    plt.title("My img")
    plt.xlabel("Pixels (X axis)")
    plt.ylabel("Pixels (Y axis)")
    plt.axis("on")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 transpose_image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    img = ft_load(image_path)
    printShape(img)

    if img is not None:
        img_array = np.array(img)
        print_img(img_array)
        print_img(ft_invert(img_array))
        print_img(ft_red(img_array))
        print_img(ft_green(img_array))
        print_img(ft_blue(img_array))
        print_img(ft_grey(img_array))