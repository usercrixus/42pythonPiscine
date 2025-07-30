import matplotlib.pyplot as plt
from load_csv import load
import matplotlib.ticker as ticker


def main():
    df = load("population_total.csv")
    if df is None:
        print("Error: Could not load dataset.")
        return

    # 🟦 Change these if needed
    my_country = "France"
    other_country = "Belgium"

    if my_country not in df['country'].values:
        print(f"Country '{my_country}' not found in dataset.")
        return
    if other_country not in df['country'].values:
        print(f"Country '{other_country}' not found in dataset.")
        return

    # ✅ Get only year columns between 1800 and 2050
    years = [col for col in df.columns
             if col.isdigit() and 1800 <= int(col) <= 2050]

    # Get population values
    my_values = df[df['country'] == my_country][years].iloc[0]\
        .str.replace('M', '').astype(float) * 1_000_000
    other_values = df[df['country'] == other_country][years].iloc[0]\
        .str.replace('M', '').astype(float) * 1_000_000

    # Plot
    plt.plot(years, my_values, label=my_country)
    plt.plot(years, other_values, label=other_country)
    plt.title(f"Population Comparison: {my_country} vs {other_country}")
    plt.xlabel("Year")
    plt.ylabel("Population (in millions)")
    plt.xticks([years[i] for i in range(0, len(years),
                                        len(years)//8)], rotation=45)
    plt.gca().yaxis.set_major_formatter
    (ticker.FuncFormatter(lambda x, _: f"{int(x / 1_000_000)}M"))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
