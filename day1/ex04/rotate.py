#!/usr/bin/env python3
from load_image import zoom
import numpy as np
import matplotlib.pyplot as plt
import math


def rotate_image(path: str, angle: int) -> np.ndarray:
    """
    Rotate an image by a given angle.

    Parameters:
    path (str): The file path to the image. The image should be in
    a format supported by OpenCV (e.g., JPEG, PNG).
    angle (int): The rotation angle in degrees. Must be a positive integer.

    Returns:
    np.ndarray: The rotated image as a 3D NumPy array.
    """
    image = zoom(path, 2)

    h, w = image.shape[:2]
    center_y, center_x = h // 2, w // 2

    rotate = np.zeros_like(image)

    cos_t = math.cos(np.radians(angle))
    sin_t = math.sin(np.radians(angle))

    for y in range(h):
        for x in range(w):
            y0 = y - center_y
            x0 = x - center_x

            x1 = cos_t * x0 + sin_t * y0
            y1 = -sin_t * x0 + cos_t * y0

            x_src = int(x1 + center_x)
            y_src = int(y1 + center_y)

            if 0 <= x_src < w and 0 <= y_src < h:
                rotate[y, x] = image[y_src, x_src]

    print(f"Rotated image shape: {rotate.shape}")
    print(rotate)

    return rotate


if __name__ == "__main__":
    try:
        rotated_image = rotate_image("../images/animal.jpeg", -90)
        if rotated_image.size > 0:
            plt.imshow(rotated_image, cmap='gray')
            plt.show()
    except Exception as e:
        print(f"Error occurred: {e}")
    except KeyboardInterrupt:
        print("Process interrupted by user.")
