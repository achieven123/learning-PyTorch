import numpy as np

X = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])

Y = np.array([1, 2, 3, 4, 5])

print(X * Y)

X = X.flatten()

print(X)
print(X[np.array([0, 5])])
print(X > 10)
print(X[X > 10])
