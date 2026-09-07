import numpy as np

sales = np.array([1200, 950, 1800, 400, 2200, 1600, 300, 1750])

# basic statistics
print("sum:", sales.sum())
print("mean:", sales.mean())
print("median:", np.median(sales))
print("std dev:", sales.std())
print("min/max:", sales.min(), sales.max())
print("variance:", sales.var())

# positions of the minimum and maximum
print("index of max:", sales.argmax())
print("index of min:", sales.argmin())

# sorting and sort positions
print("sorted:", np.sort(sales))
print("sorted indices:", np.argsort(sales))   # useful when you need to sort OTHER arrays the same way

# rounding and limits
prices = np.array([19.995, 5.501, 100.004, 49.999])
print(np.round(prices, 2))
print(np.clip(prices, 10, 60))   # cap values between 10 and 60

# cumulative values
daily = np.array([100, 150, 80, 200, 90])
print("running total:", np.cumsum(daily))
print("running max so far:", np.maximum.accumulate(daily))

# random values
rng = np.random.default_rng(seed=42)
random_scores = rng.integers(low=0, high=100, size=10)
print(random_scores)

random_floats = rng.normal(loc=50, scale=10, size=5)
print(np.round(random_floats, 2))

# dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("dot product:", np.dot(a, b))
