import numpy as np


x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

print(w * x)  # 넘파이에서 두 배열의 원소 수가 같다면, 각 원소끼리 곱함
print(np.sum(w * x))
print(np.sum(w * x) + b)
