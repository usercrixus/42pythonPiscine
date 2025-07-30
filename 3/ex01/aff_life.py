import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    df = load("life_expectancy_years.csv")
    if df is None:
        print("Error: Could not load dataset.")
        return

    country = "France"  # <-- Change to your campus country if needed
    if country not in df['country'].values:
        print(f"Error: Country '{country}' not found in dataset.")
        return

    # Extract years (all columns except 'country')
    years = df.columns[1:]
    # Extract values as float (not strings)
    values = df[df['country'] == country].values.flatten()[1:].astype(float)

    # Only display 8 evenly spaced ticks
    num_ticks = 8
    indices = np.linspace(0, len(years) - 1, num=num_ticks, dtype=int)
    selected_years = [years[i] for i in indices]

    # Plot
    plt.plot(years, values, label=country)
    plt.title(f"Life Expectancy in {country}")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (years)")
    plt.xticks(indices, selected_years, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
