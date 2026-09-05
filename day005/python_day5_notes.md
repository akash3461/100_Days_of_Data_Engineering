# Day 5 notes - Pandas

## reading data in

pd.read_csv("file.csv") and pd.read_json("file.json") load data into a DataFrame.
After loading always check it before doing anything else:

    df.head()      first 5 rows
    df.shape       (rows, cols)
    df.dtypes      what type each column is
    df.info()      structure + null counts
    df.describe()  stats for number columns

useful read_csv args: usecols, nrows, dtype, na_values - forgot these a bunch of
times so writing them down. usecols to only grab certain columns, nrows if the
file is huge and you just want a preview, dtype to force a column's type,
na_values if the file uses something weird like "N/A" or "-" for missing.

## filtering & sorting

filter by putting a condition inside df[ ]:

    df[df["category"] == "Electronics"]

combining conditions needs & (and) or | (or), and EACH condition needs its own
brackets or it just breaks:

    df[(df["price"] > 1000) & (df["region"] == "North")]

.isin() is nice when checking against a list of values instead of chaining a
bunch of ==. .loc lets you filter rows and grab specific columns at the same
time which saves a line.

sort_values("col") sorts, ascending=False for descending. can pass a list of
columns + a list of ascending flags to sort by more than one thing.

gotcha: category column had "electronics" and "Electronics" mixed in the data,
so a plain == filter misses half of them. had to do .str.lower() first.

## groupby + aggregation

this is basically "split into groups, do a calc per group, combine it back."

    df.groupby("region")["revenue"].sum()

can pass a list to .agg() for multiple stats at once (sum, mean, count etc),
or use the named version so the output columns aren't ugly:

    df.groupby("region").agg(total=("revenue","sum"), orders=("order_id","count"))

.transform() is different from .agg() - agg collapses rows down to one per
group, transform keeps every original row but attaches the group value to it.
useful when you want to compare a row to its group's average without losing
the row-level detail.

## merge / concat / pivot

merge = joining two tables on a common column (like a SQL join).
- how="left" keeps everything from the left table
- how="inner" only keeps rows that matched in both
- there's also right and outer

concat = just stacking two dataframes that have the same columns, e.g. jan
sales + feb sales = one combined table. ignore_index=True so the row numbers
don't get weird/duplicated.

pivot_table = reshapes data into a grid, kind of like an excel pivot table.
index = rows, columns = columns, values = what to fill in, aggfunc = how to
combine it (sum, mean etc). fill_value=0 so empty combos show 0 instead of NaN.

## missing values & duplicates

isna().sum() shows how many missing values are in each column. then decide -
fill it or drop it. dropping is easy but you lose data, so mostly filled stuff
in instead:
- missing quantity -> assumed 1
- missing price -> filled with median (used median per-product in the capstone,
  more accurate than one global median since prices vary a lot by product)
- missing name -> "Unknown Customer" placeholder

duplicated() flags rows that are exact copies. can also check duplicates on
just SOME columns instead of the whole row using subset=[...]. drop_duplicates()
removes them, keep="first" is the default but keep="last" is there if needed.

## dates

pd.to_datetime() converts a text column into real date objects so you can
actually do date math / filtering on it. errors="coerce" is important - turns
anything that can't be parsed into NaT instead of throwing an error and killing
the whole script.

after converting you get .dt access for stuff like:

    df["order_date"].dt.year
    df["order_date"].dt.month
    df["order_date"].dt.day_name()

resample() groups by a time period (day/week/month) but needs the date set as
the index first.

BIG gotcha I ran into: the sample data had dates in different formats
(2026-01-05, 05/01/2026, 09-01-2026) plus one that was just "invalid_date".
Using format="mixed" gets most of them but it guessed 05/01/2026 as May 1st
instead of Jan 5th (month-first guess). so mixed format parsing isn't
bulletproof - if you actually know the source format you should pass it
explicitly instead of relying on pandas to guess right every time.

## the actual task - clean + aggregate script

put all of this together in 7_clean_aggregate_pipeline.py. it:
1. loads the messy sales_data.csv
2. strips whitespace + fixes casing on text columns
3. drops the one fully duplicated row
4. fills missing customer name / qty / price
5. parses the messy dates, flags what didn't parse
6. calculates revenue = qty * price
7. builds a few reports: revenue by region, revenue by category, top 5
   customers, and a region x category pivot
8. saves the cleaned data to sales_data_cleaned.csv

---

files used across all the scripts:
- sales_data.csv - the messy dataset (jan orders)
- sales_data_feb.csv - a second month, for the concat example
- customers.json - customer info, for the merge example

quick map of which script covers what:
1. read_csv_json.py
2. filtering_sorting.py
3. groupby_aggregation.py
4. merge_concat_pivot.py
5. missing_duplicates.py
6. datetime_ops.py
7. clean_aggregate_pipeline.py - the main task, combines everything above
