import pandas as pd

df = pd.read_csv("sales_data.csv")

# order_date column is a mess - some rows are 2026-01-05, some are 05/01/2026,
# some are 09-01-2026, and one is literally "invalid_date"
# errors="coerce" turns anything it cant parse into NaT instead of crashing
df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", errors="coerce")
print(df[["order_id", "order_date"]])

# check which ones failed
print(df[df["order_date"].isna()][["order_id", "order_date"]])

# pull out parts of the date
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day_name"] = df["order_date"].dt.day_name()
print(df[["order_id", "order_date", "year", "month", "day_name"]].head(6))

# filter by date range - drop the NaT rows first or comparisons get weird
valid = df.dropna(subset=["order_date"])
recent = valid[valid["order_date"] >= "2026-01-10"]
print(recent[["order_id", "order_date"]])

# date math
today = pd.Timestamp("2026-02-01")
valid = valid.copy()
valid["days_since_order"] = (today - valid["order_date"]).dt.days
print(valid[["order_id", "order_date", "days_since_order"]].head(6))

# orders per day
per_day = valid.groupby(valid["order_date"].dt.date)["order_id"].count()
print(per_day)

# resample needs a datetime index, then you can group by week/month etc
ts = valid.set_index("order_date").sort_index()
weekly = (ts["quantity"] * ts["price"]).resample("W").sum()
print(weekly)

# NOTE: 05/01/2026 got parsed as May 1st not Jan 5th because pandas guessed
# month-first when the format was mixed. worth double checking this on real data,
# better to pass the exact format if you know it instead of "mixed"
