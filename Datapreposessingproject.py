
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load datasets
matches = pd.read_csv("datasets/Matches.csv")
deliveries = pd.read_csv("datasets/Deliveries.csv")

# 2. Display datasets
print("Matches Dataset")
print(matches.head())

print("\nDeliveries Dataset")
print(deliveries.head())

# 3. Check missing values
print("\nMatches Missing Values:")
print(matches.isnull().sum())

print("\nDeliveries Missing Values:")
print(deliveries.isnull().sum())

# 4. Visualise missing values
sns.heatmap(matches.isnull(), cbar=False)
plt.title("Matches Missing Values")
plt.show()

sns.heatmap(deliveries.isnull(), cbar=False)
plt.title("Deliveries Missing Values")
plt.show()

# 5. Remove unwanted columns
matches.drop(columns=["umpire3"], errors="ignore", inplace=True)

# 6. Handle missing values
for col in matches.columns:
    if matches[col].isnull().any():
        if matches[col].dtype == "object":
            matches[col] = matches[col].fillna("Unknown")
        else:
            matches[col] = matches[col].fillna(matches[col].median())

for col in deliveries.columns:
    if deliveries[col].isnull().any():
        if deliveries[col].dtype == "object":
            deliveries[col] = deliveries[col].fillna("Unknown")
        else:
            deliveries[col] = deliveries[col].fillna(deliveries[col].median())

# 7. Find common columns
common = list(set(matches.columns) & set(deliveries.columns))
print("\nCommon Columns:")
print(common)

# 8. Merge datasets
if "id" in matches.columns and "match_id" in deliveries.columns:
    merged = pd.merge(matches, deliveries,
                      left_on="id", right_on="match_id")
    merged.to_csv("merged_dataset.csv", index=False)
    print("\nDatasets merged successfully!")

# 9. Save cleaned datasets
matches.to_csv("cleaned_matches.csv", index=False)
deliveries.to_csv("cleaned_deliveries.csv", index=False)

print("\nData preprocessing completed successfully!")
