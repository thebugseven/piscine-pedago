#!/usr/bin/env python3
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def plot_image(image: np.ndarray) -> None:
    """Plot an image using Matplotlib."""
    try:
        if not isinstance(image, np.ndarray):
            raise ValueError("Input must be a NumPy array.")
        if image.ndim != 3 or image.shape[2] != 3:
            raise ValueError("Input array must be a 3D array"
                             "with 3 channels (RGB).")

        plt.imshow(image)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(f"Error plotting image: {e}")


def ft_invert(array) -> np.array:
    """Invert the colors of an image represented as a NumPy array."""
    try:
        if not isinstance(array, np.ndarray):
            raise ValueError("Input must be a NumPy array.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("Input array must be a 3D array "
                             "with 3 channels (RGB).")

        inverted = 255 - array
        plot_image(inverted)
        return inverted
    except Exception as e:
        print(f"Error inverting image: {e}")
        return np.array([])


def ft_red(array) -> np.array:
    """Extract the red channel from an image represented as a NumPy array."""
    try:
        if not isinstance(array, np.ndarray):
            raise ValueError("Input must be a NumPy array.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("Input array must be a 3D array "
                             "with 3 channels (RGB).")

        red_channel = array.copy()
        red_channel[:, :, 1:] = 0
        plot_image(red_channel)
        return red_channel
    except Exception as e:
        print(f"Error extracting red channel: {e}")
        return np.array([])


def ft_green(array) -> np.array:
    """Extract the green channel from an image represented as a NumPy array."""
    try:
        if not isinstance(array, np.ndarray):
            raise ValueError("Input must be a NumPy array.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("Input array must be a 3D array "
                             "with 3 channels (RGB).")

        green_channel = array.copy()
        green_channel[:, :, [0, 2]] = 0
        plot_image(green_channel)
        return green_channel
    except Exception as e:
        print(f"Error extracting green channel: {e}")
        return np.array([])


def ft_blue(array) -> np.array:
    """Extract the blue channel from an image represented as a NumPy array."""
    try:
        if not isinstance(array, np.ndarray):
            raise ValueError("Input must be a NumPy array.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("Input array must be a 3D array "
                             "with 3 channels (RGB).")

        blue_channel = array.copy()
        blue_channel[:, :, :2] = 0
        plot_image(blue_channel)
        return blue_channel
    except Exception as e:
        print(f"Error extracting blue channel: {e}")
        return np.array([])


def ft_grey(array) -> np.array:
    """Convert an image represented as a NumPy array to grayscale."""
    try:
        if not isinstance(array, np.ndarray):
            raise ValueError("Input must be a NumPy array.")
        if array.ndim != 3 or array.shape[2] != 3:
            raise ValueError("Input array must be a 3D array "
                             "with 3 channels (RGB).")

        grey_channel = (0.299 * array[:, :, 0] +
                        0.587 * array[:, :, 1] +
                        0.114 * array[:, :, 2]).astype(np.uint8)
        grey_channel = np.stack((grey_channel,) * 3, axis=-1)
        plot_image(grey_channel)
        return grey_channel
    except Exception as e:
        print(f"Error converting to grayscale: {e}")
        return np.array([])


if __name__ == "__main__":
    try:
        image = ft_load("../images/landscape.jpg")
        if image.size > 0:
            ft_invert(image)
            ft_red(image)
            ft_green(image)
            ft_blue(image)
            ft_grey(image)
            print(ft_invert.__doc__)
    except Exception as e:
        print(f"Error occurred: {e}")
    except KeyboardInterrupt:
        print("Process interrupted by user.")
