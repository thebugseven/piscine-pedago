#!/usr/bin/env python3
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a Dataset object.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    dataset = load("../datasets/life_expectancy_years.csv")
    print(dataset)
