import torch
import torch.nn as nn
import torch.nn.functional as F

torch.manual_seed(1)

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])

model = nn.Linear(1, 1)

# model 출력
# print(list(model.parameters()))

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
