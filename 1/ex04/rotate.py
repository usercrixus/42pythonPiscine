from PIL import Image
import numpy as np
import matplotlib.pyplot as plt  # pip install matplotlib

def rotate(img:Image):
    try:
        img_array = np.array(img)
        if img_array is None:
            raise ValueError("No image data to process.")

        # Transpose the square (swap axes: rotate image matrix)
        # We'll transpose height and width (not channels)
        transposed = np.transpose(img_array, (1, 0, 2))  # (H, W, C) -> (W, H, C)

        print("Transposed image shape:", transposed.shape)
        print("Transposed image pixel data (RGB):\n", transposed)

        return  Image.fromarray(transposed)

    except Exception as e:
        print(f"Error processing image: {e}")
