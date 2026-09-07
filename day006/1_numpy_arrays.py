import numpy as np

# a few ways to create arrays
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

zeros = np.zeros(5)
ones = np.ones((2, 3))
range_arr = np.arange(0, 20, 2)   # start, stop, step
lin = np.linspace(0, 1, 5)        # 5 evenly spaced numbers between 0 and 1

print(zeros)
print(ones)
print(range_arr)
print(lin)

# 2d array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print("shape:", matrix.shape)
print("ndim:", matrix.ndim)
print("dtype:", matrix.dtype)

# indexing and slicing
print(a[0], a[-1])
print(a[1:4])
print(matrix[0, 2])       # row 0, col 2
print(matrix[:, 1])       # every row, column 1
print(matrix[1, :])       # row 1, every column

# reshaping
flat = np.arange(12)
reshaped = flat.reshape(3, 4)
print(reshaped)

# boolean indexing
scores = np.array([55, 90, 42, 78, 88, 30])
passing = scores[scores >= 50]
print(passing)

# numpy uses one data type per array
mixed = np.array([1, 2, "three"])
print(mixed, mixed.dtype)
