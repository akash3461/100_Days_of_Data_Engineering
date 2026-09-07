import numpy as np
import time

# numpy can do the operation on the whole array
prices = np.array([100, 250, 75, 500, 1000])
quantities = np.array([2, 1, 5, 1, 3])

totals = prices * quantities
print(totals)

# a single number is applied to every item
discounted = prices * 0.9
print(discounted)

tax_added = prices + (prices * 0.18)
print(tax_added)

# comparisons return a boolean array
expensive = prices > 200
print(expensive)

# compare a loop with vectorized code
big_array = np.arange(1_000_000)

start = time.time()
squared_loop = [x ** 2 for x in big_array]
loop_time = time.time() - start

start = time.time()
squared_vectorized = big_array ** 2
vector_time = time.time() - start

print(f"loop took {loop_time:.4f}s")
print(f"vectorized took {vector_time:.4f}s")
print(f"vectorized was about {loop_time / vector_time:.1f}x faster")

# broadcasting with different shapes
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_addition = np.array([10, 20, 30])
print(matrix + row_addition)   # row_addition gets applied to every row
