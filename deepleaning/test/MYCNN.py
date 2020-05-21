import tensorflow as tf
from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np

# 导入数据，分别为输入特征和标签
x_data = datasets.load_iris().data[:100]
y_data = datasets.load_iris().target[:100]

x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]
x_train = np.array(x_train, np.float32)
x_test = np.array(x_test, np.float32)

lr = 0.1
w = np.ones(4)
b = np.ones(1)
'''
print(x_train[:4])
[[5.1 3.5 1.4 0.2]
[4.9 3.  1.4 0.2]
[4.7 3.2 1.3 0.2]
[4.6 3.1 1.5 0.2]]
print(y_train[:4])
[0 0 0 0]
'''
for i in range(1):
    for ind in range(len(x_train)):
        print("---------------------------------")
        Y = y_train[ind]
        X = x_train[ind]
        print(w*X+b)
        # y = X * w + b
        # y = (w*X + b)
        # y = np.float32(np.argmax(np.dot(X, w) + b))
        y = np.argmax(w*X + b)
        # rav=[0,0,0]
        # rav[np.argmax(y)]=1
        # print(np.argmax(y))
        # print(rav)
        # loss=(y_ - y)^2 = (y_ - X * w - b)^2
        # dloss/dw =2 * X * (y_ - X * w - b)
        # dloss/db =2 * (y_ - X * w - b)
        # w_ = w  - 2 * X * lr * (y_ - X * w - b)
        # b_ = b  - 2 * lr * (y_ - X * w - b)
        # print(np.array(2 * lr * X*(np.array([y])- y_)))
        w = w - 2 * lr * X*(y -Y)
        b = b - 2 * lr * (y - Y)

        # print(w)
        # print(b)
        pass
    pass
pass

