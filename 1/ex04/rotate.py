from PIL import Image
import numpy as np
import sys
from load_image import ft_load, printShape
import matplotlib.pyplot as plt


def my_transpose(img_array: np.ndarray) -> np.ndarray:
    "rotate the matrix"
    h, w, c = img_array.shape
    # Create empty array with shape (w, h, c)
    transposed = np.zeros((w, h, c), dtype=img_array.dtype)

    for i in range(h):
        for j in range(w):
            transposed[j, i] = img_array[i, j]  # swap row and column

    return transposed


def rotate(img_array: np.ndarray) -> np.ndarray:
    "rotate function"
    try:
        if img_array is None:
            raise ValueError("No image data to process.")

        # Transpose the square (swap axes: rotate image matrix)
        # We'll transpose height and width (not channels)
        transposed = my_transpose(img_array)  # (H, W, C) -> (W, H, C)
        return transposed

    except Exception as e:
        print(f"Error processing image: {e}")


def square(img_array: np.ndarray) -> np.ndarray:
    mxValue = min(img_array.shape[0], img_array.shape[1])
    return img_array[0:mxValue, 0:mxValue]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 transpose_image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    img = ft_load(image_path)

    if img is not None:
        squared = square(img)
        if squared is not None:
            rotated_img = rotate(squared)
            if rotated_img is not None:
                printShape(rotated_img)
                rotated_array = np.array(rotated_img)
                plt.imshow(rotated_array)
                plt.title("Zoomed and Transposed Image")
                plt.xlabel("Pixels (X axis)")
                plt.ylabel("Pixels (Y axis)")
                plt.axis("on")
                plt.show()
