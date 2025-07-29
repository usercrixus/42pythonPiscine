from PIL import Image
import numpy as np


def printShape(img_array: np.ndarray):
    "helper to print the shape"
    print("Image shape (H, W, C):", img_array.shape)
    print("Pixel values (RGB):\n", img_array)


def ft_load(path: str) -> np.ndarray:
    "return an img object"
    try:
        with Image.open(path) as img:
            # Ensure RGB format
            if img.mode != 'RGB':
                img = img.convert('RGB')
                print("Converted to RGB.")

            printShape(np.array(img))
            return np.array(img)

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print("Error loading image:", e)
