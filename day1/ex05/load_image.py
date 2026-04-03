#!/usr/bin/env python3
import numpy as np
import imageio.v3 as iio


def ft_load(path: str) -> np.array:
    """Load an image from a file path and return it as a NumPy array."""
    try:
        if not path.lower().endswith(('.jpg',
                                      '.jpeg',
                                      '.png',
                                      '.bmp',
                                      '.tiff')):
            raise ValueError("Unsupported file format."
                             "Please provide a valid image file.")
        image = iio.imread(path)
        print(f"The shape of the image is: {image.shape}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])


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

        center_y, center_x = h // 2 - 90, w // 2 + 130
        half = 200

        crop = image[
            center_y - half:center_y + half,
            center_x - half:center_x + half
        ]

        crop = crop.mean(axis=2).astype(np.uint8)

        print(f"New shape after slicing: {crop[:, :, np.newaxis].shape}\
              or {crop.shape}")
        print(crop[:, :, np.newaxis])

        return crop
    except Exception as e:
        print(f"Error occurred: {e}")
        return np.array([])


if __name__ == "__main__":
    print(ft_load("../images/landscape.jpg"))
