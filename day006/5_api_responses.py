import json
import pandas as pd
import numpy as np

# sample nested response

api_response = {
    "status": "ok",
    "page": 1,
    "results": [
        {
            "order_id": 201,
            "customer": {"name": "Aarav Sharma", "membership": "Gold"},
            "items": [{"product": "Laptop", "qty": 1, "price": 55000}],
            "region": "North"
        },
        {
            "order_id": 202,
            "customer": {"name": "Isha Patel", "membership": "Silver"},
            "items": [{"product": "Mouse", "qty": 2, "price": 500}, {"product": "Keyboard", "qty": 1, "price": 1200}],
            "region": "South"
        },
        {
            "order_id": 203,
            "customer": {"name": "Rohan Verma", "membership": "Gold"},
            "items": [{"product": "Monitor", "qty": 1, "price": 8000}],
            "region": None
        },
    ]
}

with open("api_response_sample.json", "w") as f:
    json.dump(api_response, f, indent=2)

records = api_response["results"]

# flatten the customer fields
flat = pd.json_normalize(records)
print(flat)
print(flat.columns.tolist())

# flatten the items and keep the order fields
items_flat = pd.json_normalize(
    records,
    record_path="items",
    meta=["order_id", ["customer", "name"], "region"],
)
print(items_flat)

items_flat["revenue"] = items_flat["qty"] * items_flat["price"]
print(items_flat)

revenue_arr = items_flat["revenue"].to_numpy()
print("total revenue (numpy sum):", np.sum(revenue_arr))

# check for missing regions
missing_region = flat["region"].isna().sum()
print(f"\n{missing_region} order(s) missing a region - probably worth flagging or fixing before loading downstream")
