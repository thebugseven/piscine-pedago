#!/usr/bin/env python3
from load_csv import load
import matplotlib.pyplot as plt


def plot_life_expectancy(path: str) -> None:
    """Plot life expectancy data from a CSV file.

    Args:
        path (str): The path to the CSV file containing life expectancy data.
    """
    try:
        dataset = load(path)
        if dataset.empty:
            print("No data to plot.")
            return

        plt.figure(figsize=(10, 6))
        if "France" not in dataset.index:
            print("France not found in the dataset.")
            return
        data = dataset.loc["France"]
        plt.plot(data.index, data.values)
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        plt.xticks(data.index[::40])
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(f"Error plotting life expectancy: {e}")


if __name__ == "__main__":
    plot_life_expectancy("../datasets/life_expectancy_years.csv")