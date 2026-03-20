#!/usr/bin/env python3
import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """Calculate the BMI for a list of heights and weights.

    Args:
        height: A list of heights in centimeters.
        weight: A list of weights in kilograms.

    Returns:
        A list of BMIs corresponding to the input heights and weights.
    """
    try:
        height = np.array(height)
        weight = np.array(weight)
        bmi = weight / (height ** 2)
        return bmi.tolist()
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a BMI limit to a list of BMIs.

    Args:
        bmi: A list of BMIs.
        limit: The BMI limit to apply.

    Returns:
        A list of booleans indicating whether each BMI is above
        the limit.
    """
    try:
        bmi = np.array(bmi)
        return (bmi > limit).tolist()
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


if __name__ == "__main__":
    heights = [1.70, 1.80, 1.90]
    weights = [70, 80, 90]
    bmi_values = give_bmi(heights, weights)
    print("BMI values:", bmi_values)

    limit = 25
    above_limit = apply_limit(bmi_values, limit)
    print(f"BMIs above {limit}:", above_limit)
