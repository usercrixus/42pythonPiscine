import numpy as np

def ft_invert(array) -> np.ndarray:
    return 255 - array  # allowed: -, =

def ft_red(array) -> np.ndarray:
    result = array * 0  # allowed: *, =
    result[:, :, 0] = array[:, :, 0]  # keep red
    return result

def ft_green(array) -> np.ndarray:
    result = array - array  # allowed: -, = (creates zeros)
    result[:, :, 1] = array[:, :, 1]  # keep green
    return result

def ft_blue(array) -> np.ndarray:
    # allowed only: = → must construct manually
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result

def ft_grey(array) -> np.ndarray:
    # Cast to a wider type to prevent overflow
    r = array[:, :, 0].astype(np.uint16)
    g = array[:, :, 1].astype(np.uint16)
    b = array[:, :, 2].astype(np.uint16)

    grey = (r * 77 + g * 150 + b * 29) // 256

    result = np.zeros_like(array)
    result[:, :, 0] = grey.astype(np.uint8)
    result[:, :, 1] = grey.astype(np.uint8)
    result[:, :, 2] = grey.astype(np.uint8)

    return result
