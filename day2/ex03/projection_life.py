#!/usr/bin/env python3
from load_csv import load
import matplotlib.pyplot as plt


def plot_projection() -> None:
    """Plot life expectancy projections from a CSV file.

    Args:
        path (str): The path to the CSV file containing life expectancy data.
    """
    try:
        data_income = load(
            "../datasets/"
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        data_life = load("../datasets/life_expectancy_years.csv")

        if data_income.empty or data_life.empty:
            print("No data to plot.")
            return

        year = "1900"

        plt.figure(figsize=(10, 6))
        plt.scatter(data_income[year], data_life[year], color='blue')

        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")

        ax = plt.gca()
        ax.set_xscale('log')
        ax.set_xticks([300, 1000, 10000])
        ax.set_xticklabels(['300', '1k', '10k'])

        plt.show()
    except Exception as e:
        print(f"Error plotting life expectancy: {e}")


if __name__ == "__main__":
    plot_projection()
