from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  # pip install matplotlib

def my_transpose(img_array: np.ndarray) -> np.ndarray:
    h, w, c = img_array.shape
    # Create empty array with shape (w, h, c)
    transposed = np.zeros((w, h, c), dtype=img_array.dtype)

    for i in range(h):
        for j in range(w):
            transposed[j, i] = img_array[i, j]  # swap row and column

    return transposed


def rotate(img:Image):
    try:
        img_array = np.array(img)
        if img_array is None:
            raise ValueError("No image data to process.")

        # Transpose the square (swap axes: rotate image matrix)
        # We'll transpose height and width (not channels)
        transposed = my_transpose(img_array)  # (H, W, C) -> (W, H, C)
        return  Image.fromarray(transposed)

    except Exception as e:
        print(f"Error processing image: {e}")
