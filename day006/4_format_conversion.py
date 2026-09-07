import pandas as pd
import os
from pathlib import Path

# cleaned file from day 5
data_file = Path(__file__).parent.parent / "day005" / "sales_data_cleaned.csv"
df = pd.read_csv(data_file)
print(f"loaded {len(df)} rows, {len(df.columns)} columns")
print(df.dtypes)

df.to_csv("format_test.csv", index=False)

df.to_json("format_test.json", orient="records")

parquet_written = False
try:
    df.to_parquet("format_test.parquet", index=False)
    parquet_written = True
except ImportError as e:
    print("couldn't write parquet, missing engine:", e)
    print("run: pip install pyarrow")

def get_size_kb(path):
    return os.path.getsize(path) / 1024

csv_size = get_size_kb("format_test.csv")
json_size = get_size_kb("format_test.json")

print(f"\ncsv:  {csv_size:.2f} KB")
print(f"json: {json_size:.2f} KB")

if parquet_written:
    parquet_size = get_size_kb("format_test.parquet")
    print(f"parquet: {parquet_size:.2f} KB")
    print(f"\nparquet is {csv_size / parquet_size:.1f}x smaller than csv")
    print(f"json is {json_size / csv_size:.1f}x bigger than csv")

    import time

    start = time.time()
    pd.read_csv("format_test.csv")
    csv_read_time = time.time() - start

    start = time.time()
    pd.read_parquet("format_test.parquet")
    parquet_read_time = time.time() - start

    print(f"\ncsv read time:     {csv_read_time:.4f}s")
    print(f"parquet read time: {parquet_read_time:.4f}s")
else:
    print("\nskipped parquet size/speed comparison since it wasn't written")

# notes on why the size difference happens:
# - csv/json are plain text, every value gets written out as a string
# - parquet is columnar + compressed + stores real data types, so numbers
#   don't need to be re-parsed as text every time you read the file
# - json is usually the biggest of the three because of all the repeated
#   key names on every single row
