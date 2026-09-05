import pandas as pd

df = pd.read_csv("sales_data.csv")
df["revenue"] = df["quantity"] * df["price"]

customers = pd.read_json("customers.json")
feb = pd.read_csv("sales_data_feb.csv")

# merge - joining on customer_name, keeping all sales rows even if no match found
merged = df.merge(customers, on="customer_name", how="left")
print(merged[["order_id", "customer_name", "membership", "revenue"]].head(6))

# inner join only keeps rows that matched on both sides
inner = df.merge(customers, on="customer_name", how="inner")
print(f"inner join kept {len(inner)} out of {len(df)} rows")

# concat just stacks rows on top of each other (jan + feb data)
all_sales = pd.concat([df, feb], ignore_index=True)
print(f"jan has {len(df)} rows, feb has {len(feb)}, combined {len(all_sales)}")
print(all_sales.tail())

# pivot table - like excel pivot, region as rows, category as columns
pivot = df.pivot_table(index="region", columns="category", values="revenue",
                        aggfunc="sum", fill_value=0)
print(pivot)

# can also pass multiple aggfuncs
pivot2 = df.pivot_table(index="region", values="revenue", aggfunc=["sum", "mean", "count"])
print(pivot2)
