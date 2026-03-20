#!/usr/bin/env python3
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list of family members from start to end index.

    Args:
        family: A list of family members.
        start: The starting index for slicing.
        end: The ending index for slicing.

    Returns:
        A list of family members from the specified range.
    """
    try:
        assert isinstance(family, list), "Family must be a list"
        assert isinstance(start, int), "Start index must be an integer"
        assert isinstance(end, int), "End index must be an integer"

        print(f"My shape is : {np.array(family).shape}")
        my_slice = slice(start, end)
        family = np.array(family)[my_slice]
        print(f"My new shape is : {family.shape}")
        return family.tolist()
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


if __name__ == "__main__":
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 85.3]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
