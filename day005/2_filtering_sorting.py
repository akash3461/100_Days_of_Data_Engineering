import pandas as pd

df = pd.read_csv("sales_data.csv")

# filter for electronics only
electronics = df[df["category"] == "Electronics"]
print(electronics[["order_id", "product", "category"]])

# problem is category has mixed casing (Electronics vs electronics), so this misses rows
# fix with .str.lower()
electronics_fixed = df[df["category"].str.lower() == "electronics"]
print(electronics_fixed[["order_id", "product", "category"]])

# combining conditions - need brackets around each one or it breaks
north_high_value = df[(df["price"] > 1000) & (df["region"] == "North")]
print(north_high_value[["order_id", "product", "price", "region"]])

south_or_west = df[(df["region"] == "South") | (df["region"] == "West")]
print(south_or_west[["order_id", "region"]])

# isin is handy when checking multiple values
picked = df[df["product"].isin(["Laptop", "Monitor"])]
print(picked[["order_id", "product"]])

# .loc lets u filter rows and pick columns together
qty_filter = df.loc[df["quantity"] > 2, ["order_id", "product", "quantity"]]
print(qty_filter)

# sorting
by_price = df.sort_values("price", ascending=False)
print(by_price[["order_id", "product", "price"]].head())

# sort by more than one column
multi_sort = df.sort_values(["region", "price"], ascending=[True, False])
print(multi_sort[["region", "product", "price"]].head(8))
