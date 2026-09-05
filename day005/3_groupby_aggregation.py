import pandas as pd

df = pd.read_csv("sales_data.csv")
df["revenue"] = df["quantity"] * df["price"]

# total revenue per region
by_region = df.groupby("region")["revenue"].sum()
print(by_region)

# multiple stats at once
region_stats = df.groupby("region")["revenue"].agg(["sum", "mean", "count"])
print(region_stats)

# group by two columns
cat_region = df.groupby(["category", "region"])["revenue"].sum()
print(cat_region)

# giving the output columns proper names instead of the default
summary = df.groupby("region").agg(
    total_revenue=("revenue", "sum"),
    avg_qty=("quantity", "mean"),
    orders=("order_id", "count"),
)
print(summary)

print(summary.sort_values("total_revenue", ascending=False))

# transform puts the group result back onto every row instead of collapsing
df["region_avg_revenue"] = df.groupby("region")["revenue"].transform("mean")
print(df[["order_id", "region", "revenue", "region_avg_revenue"]].head(6))

# which product sold the most units
best_sellers = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
print(best_sellers)
