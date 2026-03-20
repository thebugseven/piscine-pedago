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


if __name__ == "__main__":
    print(ft_load("landscape.jpg"))
