import pandas as pd

pd.set_option("display.width", 100)

# messy stuff in sales_data.csv:
# - "electronics" vs "Electronics" casing
# - extra spaces around names
# - order 101 is duplicated
# - missing customer_name, quantity, price in a few rows
# - order_date has 3 different formats + one invalid value


def load_data(path):
    df = pd.read_csv(path)
    print(f"loaded {len(df)} rows from {path}")
    return df


def clean_text(df):
    df = df.copy()
    df["customer_name"] = df["customer_name"].str.strip()
    df["product"] = df["product"].str.strip()
    df["category"] = df["category"].str.strip().str.title()
    df["region"] = df["region"].str.strip()
    return df


def remove_dupes(df):
    before = len(df)
    df = df.drop_duplicates()
    print(f"dropped {before - len(df)} duplicate row(s)")
    return df


def fill_missing(df):
    df = df.copy()
    df["customer_name"] = df["customer_name"].fillna("Unknown Customer")
    df["quantity"] = df["quantity"].fillna(1)
    # fill price using the median for that specific product, not a global median
    df["price"] = df.groupby("product")["price"].transform(lambda s: s.fillna(s.median()))
    return df


def fix_dates(df):
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", errors="coerce")
    bad = df["order_date"].isna().sum()
    if bad:
        print(f"{bad} row(s) had a date that wouldn't parse, set to NaT")
    return df


def add_calculated_cols(df):
    df = df.copy()
    df["revenue"] = df["quantity"] * df["price"]
    df["month"] = df["order_date"].dt.to_period("M")
    return df


def make_reports(df):
    by_region = (
        df.groupby("region")
        .agg(total_revenue=("revenue", "sum"), order_count=("order_id", "count"))
        .sort_values("total_revenue", ascending=False)
    )

    by_category = (
        df.groupby("category")
        .agg(total_revenue=("revenue", "sum"), total_qty=("quantity", "sum"))
        .sort_values("total_revenue", ascending=False)
    )

    top_customers = (
        df.groupby("customer_name")["revenue"].sum().sort_values(ascending=False).head(5)
    )

    pivot = df.pivot_table(index="region", columns="category", values="revenue",
                            aggfunc="sum", fill_value=0)

    return by_region, by_category, top_customers, pivot


def run(path):
    df = load_data(path)
    df = clean_text(df)
    df = remove_dupes(df)
    df = fill_missing(df)
    df = fix_dates(df)
    df = add_calculated_cols(df)

    print("\ncleaned data preview:")
    print(df[["order_id", "customer_name", "product", "category", "quantity",
               "price", "order_date", "revenue"]].head(8))

    by_region, by_category, top_customers, pivot = make_reports(df)

    print("\nrevenue by region:")
    print(by_region)

    print("\nrevenue by category:")
    print(by_category)

    print("\ntop 5 customers:")
    print(top_customers)

    print("\nregion x category pivot:")
    print(pivot)

    return df


if __name__ == "__main__":
    cleaned = run("sales_data.csv")
    cleaned.to_csv("sales_data_cleaned.csv", index=False)
    print("\nsaved cleaned data to sales_data_cleaned.csv")
