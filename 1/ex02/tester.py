import sys
from load_image import ft_load

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print("Usage: python3 load_image.py <image_path>")
        sys.exit(1)
    else:
        ft_load(argv[1])
