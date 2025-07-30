import numpy as np
import matplotlib.pyplot as plt


def print_img(img_array: np.ndarray):
    "helper to displqy img"
    plt.imshow(img_array)
    plt.title("My img")
    plt.xlabel("Pixels (X axis)")
    plt.ylabel("Pixels (Y axis)")
    plt.axis("on")
    plt.show()


def ft_invert(array) -> np.ndarray:
    "invert colors"
    print_img(255 - array)
    return 255 - array  # allowed: -, =


def ft_red(array) -> np.ndarray:
    "red filter"
    result = array * 0  # allowed: *, =
    result[:, :, 0] = array[:, :, 0]  # keep red
    print_img(result)
    return result


def ft_green(array) -> np.ndarray:
    "green filter"
    result = array - array  # allowed: -, = (creates zeros)
    result[:, :, 1] = array[:, :, 1]  # keep green
    print_img(result)
    return result


def ft_blue(array) -> np.ndarray:
    "blue filter"
    # allowed only: = → must construct manually
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    print_img(result)
    return result


def ft_grey(array) -> np.ndarray:
    "grey filter"
    # Cast to a wider type to prevent overflow
    r = array[:, :, 0].astype(np.uint16)
    g = array[:, :, 1].astype(np.uint16)
    b = array[:, :, 2].astype(np.uint16)

    grey = (r * 77 + g * 150 + b * 29) // 256

    result = np.zeros_like(array)
    result[:, :, 0] = grey.astype(np.uint8)
    result[:, :, 1] = grey.astype(np.uint8)
    result[:, :, 2] = grey.astype(np.uint8)

    print_img(result)
    return result
