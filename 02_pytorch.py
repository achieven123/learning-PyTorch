import torch

# t = torch.FloatTensor([0., 1., 2., 3., 4., 5., 6.])
# print(t)

# print(t.dim())
# print(t.size())

# print(t[1:-2])

t = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]
                       ])

# print(t)
# print(t.dim())
# print(t.size())

# print(t[:, 1])
# print(t[:, 1].size())
# print(t[:, :1])


# Broadcasting(브로드캐스팅)

# m1 = torch.FloatTensor([[1, 2]])
# m2 = torch.FloatTensor([[3], [4]])

# print(m1.dim())
# print(m1 + m2)

t = torch.FloatTensor([[1, 2], [3, 4]])

print(t.mean(dim = 0))

