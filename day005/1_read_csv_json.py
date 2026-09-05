import pandas as pd

# loading the sales csv
df = pd.read_csv("sales_data.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# quick check on the data
df.info()
print(df.describe())

# now loading the customers json file
customers = pd.read_json("customers.json")
print(customers.head())
print(customers.shape)

# some useful args for read_csv i keep forgetting:
# usecols=[...] -> only load certain columns
# nrows=100 -> only first 100 rows, good for huge files
# dtype={"order_id": str} -> force a column type
# na_values=["N/A"] -> treat custom strings as missing
