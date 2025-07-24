from PIL import Image # pip install pillow
import numpy as np # pip install numpy

def ft_load(path: str) -> Image:
    try:
        with Image.open(path) as img:
            # Ensure RGB format
            if img.mode != 'RGB':
                img = img.convert('RGB')
                print("Converted to RGB.")

            return img.copy()

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print("Error loading image:", e)