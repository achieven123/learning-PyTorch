import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b  # 넘파이에서 두 배열의 원소 수가 같다면, 각 원소끼리 곱함

    if tmp <= 0:
        return 0
    else:
        return 1


print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1


print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = 0.2
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1.0, 1.0])
    b = -0.5
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1


print(XOR(1, 1))
