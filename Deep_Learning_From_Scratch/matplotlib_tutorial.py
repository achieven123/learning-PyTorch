import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# x = np.arange(0, 6, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label="sin")
# plt.plot(x, y2, linestyle="--", label="cos")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title('sin & cos')
# plt.legend()
# plt.show()

img = imread('C:\GitHub\learning-PyTorch\Deep_Learning_From_Scratch\고양이.jpg')

plt.imshow(img)
plt.show()
