import pandas as pd

df = pd.read_csv("sales_data.csv")

# how many missing values per column
print(df.isna().sum())

# rows with at least one missing value
print(df[df.isna().any(axis=1)])

filled = df.copy()

# quantity missing -> assume 1 unit
filled["quantity"] = filled["quantity"].fillna(1)

# price missing -> fill with median price
med_price = filled["price"].median()
filled["price"] = filled["price"].fillna(med_price)

filled["customer_name"] = filled["customer_name"].fillna("Unknown Customer")

print(filled.isna().sum())

# dropna removes rows instead of filling - use carefully, loses data
dropped = df.dropna()
print(f"{len(df)} rows before dropna, {len(dropped)} after")

# only drop if a specific column is missing
dropped_price_only = df.dropna(subset=["price"])
print(f"dropna on price only: {len(dropped_price_only)} rows")

# duplicates
print(df[df.duplicated()])
print("dupe count:", df.duplicated().sum())

# check dupes on specific columns instead of the whole row
print(df.duplicated(subset=["customer_name", "product"]).sum())

no_dupes = df.drop_duplicates()
print(f"{len(df)} -> {len(no_dupes)} after dropping dupes")

# keep last occurrence instead of first
keep_last = df.drop_duplicates(keep="last")
print(len(keep_last))
