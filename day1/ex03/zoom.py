#!/usr/bin/env python3
import numpy as np
import cv2 as cv
import imageio.v3 as iio
from load_image import ft_load


def zoom(path: str, factor: int) -> np.ndarray:
    """
    Zooms in on an image by a given factor.

    Parameters:
    path (str): The file path to the image. The image should be in
    a format supported by OpenCV (e.g., JPEG, PNG).
    factor (int): The zoom factor. Must be a positive integer.

    Returns:
    np.ndarray: The zoomed-in image as a 3D NumPy array.
    """
    try:
        if factor <= 0:
            raise ValueError("Zoom factor must be a positive integer.")
        image = ft_load(path)
        if image.size == 0:
            raise ValueError("Failed to load image.")
        print(image)

        h, w = image.shape[:2]

        crop = image[h//4:3*h//4, w//4:3*w//4]

        zoomed = cv.resize(crop, (w, h), interpolation=cv.INTER_LINEAR)
        print(f"New shape after slicing: {crop.shape}")

        iio.imwrite("zoomed_image.jpeg", zoomed)

        return zoomed
    except Exception as e:
        print(f"Error occurred: {e}")
        return np.array([])


if __name__ == "__main__":
    zoom("animal.jpeg", 2)
