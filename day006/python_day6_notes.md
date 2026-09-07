# Day 6 notes - NumPy + Data Formats

## arrays

numpy's main thing is the array - like a python list but faster and only
holds one data type. creating them:

    np.array([1,2,3])
    np.zeros(5)
    np.ones((2,3))
    np.arange(0, 20, 2)      start, stop, step
    np.linspace(0, 1, 5)     5 evenly spaced numbers

check shape/type stuff with .shape, .ndim, .dtype. indexing/slicing works
basically like lists but you can do it per-dimension:

    matrix[0, 2]     row 0, col 2
    matrix[:, 1]     every row, just column 1

reshape() changes the shape without changing the actual data, good for
turning a flat list into a grid. boolean indexing is the one that actually
comes up a lot - scores[scores >= 50] just gives you back the values that
pass the condition, no loop needed.

one gotcha - if you mix types in one array (like a number and a string)
numpy upcasts everything to the same type instead of erroring, so watch
out for that.

## vectorized operations

this is the actual reason people use numpy instead of plain loops. instead
of looping over a list to multiply two things together, you just do:

    totals = prices * quantities

and it applies the operation to every matching pair at once. same for adding,
comparing, etc - all element-wise. "broadcasting" is when you combine an
array with a single number and it applies to every element:

    discounted = prices * 0.9

ran a quick loop-vs-vectorized timing test on 1 million numbers and vectorized
was like 3x faster in this sandbox (real difference on bigger data is usually
way more than that, this was a small example).

broadcasting also works between different shaped arrays as long as the
shapes are compatible - e.g. adding a 1d array to every row of a 2d one.

## numerical ops

numpy has most stats stuff built in directly on the array, don't need pandas
for basic numbers:

    arr.sum() / .mean() / .std() / .min() / .max() / .var()
    np.median(arr)
    arr.argmax() / argmin()    -> index of the max/min, not the value itself
    np.sort(arr) / np.argsort(arr)

argsort is handy when you need to sort a DIFFERENT array using the same
order as this one.

np.round() and np.clip() for rounding and capping values into a range.
cumsum() gives a running total, useful for anything time-series-y.

random number generation:

    rng = np.random.default_rng(seed=42)
    rng.integers(0, 100, size=10)
    rng.normal(loc=50, scale=10, size=5)

using a seed makes it reproducible - same numbers every time you run it,
good for testing.

## csv / json / parquet

the actual day 6 task was converting the same data between formats and
comparing file sizes. did this using the cleaned sales data from day 5.

    df.to_csv("file.csv", index=False)
    df.to_json("file.json", orient="records")
    df.to_parquet("file.parquet", index=False)     needs pyarrow installed

results (on the small 13-row test file):
- csv: 1.04 KB
- json: 2.49 KB (json is bigger cause it repeats every column name on
  every single row)
- parquet: couldn't actually test this in the sandbox, no internet to
  install pyarrow. but on real datasets parquet is usually way smaller
  than both, and way faster to read back too

why parquet wins on bigger data:
- its columnar, so it stores each column contiguously instead of row by row
- compressed by default
- keeps the actual data types instead of re-writing everything as text,
  so it doesn't need to reparse numbers/dates every time you load it

csv/json are still fine for small stuff or for interoperability (like
exporting for someone using excel), but for actual pipelines parquet is the
better default once the data gets any real size.

need to `pip install pyarrow` on my own machine before this'll fully work -
added that to requirements.txt.

## working with API responses

apis basically always return nested json, not something already
table-shaped. the format is usually something like:

    {
      "results": [
        {"order_id": 1, "customer": {"name": "x"}, "items": [...]}
      ]
    }

pd.json_normalize() flattens the nested dict parts into columns
automatically (customer.name, customer.membership etc). if a field is a
LIST of dicts (like items, where one order can have multiple products),
normalize that separately with record_path, and use meta= to keep the
outer fields (order_id, region) attached to each row.

after flattening it's just a normal dataframe so all the usual pandas/numpy
stuff works - added a revenue column, converted it to a numpy array,
checked for missing values the same way as always.

practical thing worth remembering: always check for missing/null fields
right after normalizing - the test response had a null region and it's the
kind of thing that gets missed once its buried in a nested response.

---

## quick script map

1. numpy_arrays.py - creating arrays, indexing/slicing, reshape, boolean filtering
2. vectorized_ops.py - vectorized math vs loops, broadcasting, speed comparison
3. numerical_ops.py - stats, sorting, rounding/clipping, cumulative sums, random numbers
4. format_conversion.py - the actual task: csv vs json vs parquet, size comparison
5. api_responses.py - flattening a nested json api response with json_normalize

files this depends on:
- sales_data_cleaned.csv (from the day 5 capstone) - used in format_conversion.py
- api_response_sample.json - gets created by api_responses.py when you run it

still need to pip install pyarrow locally to actually see the parquet
numbers, couldn't do that in this sandbox since it has no internet access.
