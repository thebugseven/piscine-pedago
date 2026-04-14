#!/usr/bin/env python3
from load_csv import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator


def plot_total(path: str) -> None:
    """Plot total population data from a CSV file.

    Args:
        path (str): The path to the CSV file containing population data.
    """
    try:
        dataset = load(path)
        if dataset.empty:
            print("No data to plot.")
            return

        if "France" not in dataset.index or "Belgium" not in dataset.index:
            print("France or Belgium not found in the dataset.")
            return
        years = list(range(1800, 2051))
        dF = dataset.loc["France", [str(y) for y in years]].str.replace(
            "M", "", regex=False
        )
        dB = dataset.loc["Belgium", [str(y) for y in years]].str.replace(
            "M", "", regex=False
        )

        dF = pd.to_numeric(dF, errors="coerce")
        dB = pd.to_numeric(dB, errors="coerce")

        plt.figure(figsize=(10, 6))
        plt.plot(years, dF, label="France")
        plt.plot(years, dB, label="Belgium")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(np.arange(1800, 2051, 40))
        plt.ylabel("Total Population")

        ax = plt.gca()

        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.yaxis.set_major_formatter(
            FuncFormatter(lambda x, _: f"{x:.0f}M")
        )

        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error plotting total population: {e}")


if __name__ == "__main__":
    plot_total("../datasets/population_total.csv")
