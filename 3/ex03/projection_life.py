import matplotlib.pyplot as plt
from load_csv import load

def main():
    # Load datasets
    income_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("life_expectancy_years.csv")
    
    if income_df is None or life_df is None:
        print("Error loading one or both datasets.")
        return

    # Check if 1900 column exists
    if "1900" not in income_df.columns or "1900" not in life_df.columns:
        print("Year 1900 not found in one of the datasets.")
        return

    # Extract country + 1900 only
    income_1900 = income_df[["country", "1900"]].copy()
    life_1900 = life_df[["country", "1900"]].copy()

    # Rename columns for clarity before merging
    income_1900.columns = ["country", "income"]
    life_1900.columns = ["country", "life_expectancy"]

    # Merge on country
    merged = income_1900.merge(life_1900, on="country")

    # Drop rows with missing or non-numeric values
    merged = merged.dropna()
    merged = merged[(merged["income"] != "..") & (merged["life_expectancy"] != "..")]

    # Convert to float
    merged["income"] = merged["income"].astype(float)
    merged["life_expectancy"] = merged["life_expectancy"].astype(float)

    # Plot
    plt.scatter(merged["income"], merged["life_expectancy"])
    plt.title("Life Expectancy vs GDP per Capita (Year 1900)")
    plt.xlabel("GDP per capita (PPP, inflation-adjusted)")
    plt.ylabel("Life Expectancy (years)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
