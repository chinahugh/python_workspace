import numpy as np
X = np.array([[-0.1, -2, -3], [-.002, .004, -.006], [1, 1, 2],
              [1, -2, -3], [-.002, .004, -.006], [10, 1, 2]], dtype=np.float32)
Y = np.array([1, 1, 0, 1, 1, 0])



m = np.array([0, 0, 0], dtype=np.float32)
b = np.array(-1, dtype=np.float32)
# y = np.sum(m*X[1] + b)
# yy = 1/(1+np.exp(-y))


def yyy(yy):
    if yy > 0.5:
        return 1
    else:
        return 0

# print(1-0&1)


def update_weights_MSE(m, b, X, Y, learning_rate):
    m_deriv = 0
    b_deriv = 0
    N = len(X)
    for _ in range(1):
        for i in range(N):
            # 计算结果
            y = np.sum(m*X[i] + b)
            # 误差
            y_2 = (Y[i]-y)**2
            print("loss :"+str(y_2))
            # 激活函数
            yy = 1/(1+np.exp(-y))
            # yy = y**3
            yyyy = 1-yyy(yy) & Y[i]
            # print("yyyy : "+str(yyyy))
            print("yy : "+str(yy))
            # print("yyy : "+str(yyy(yy)))
            # 计算偏导数为
            # -2x(y - (mx + b))
            m_deriv = -2*X[i] * (Y[i] - (m*X[i] + b))*yyyy
            # -2(y - (mx + b))
            b_deriv = np.sum(-2*(Y[i] - (m*X[i] + b)))*yyyy

            # 我们减去它，因为导数指向最陡的上升方向
            m1 = m - m_deriv * learning_rate
            b1 = m - b_deriv * learning_rate
            # 验证
            y2 = np.sum(m1*X[i] + b1)
            # 误差
            y_2_2 = (Y[i]-y2)**2
            if y_2_2 < y_2:
                m += m_deriv * learning_rate
                b += b_deriv * learning_rate
                pass
            pass
        pass
    print(m)
    print(b)
    return m, b
    pass


# print(update_weights_MSE(m, b, X, Y, 0.01))

import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1.0/(1+np.exp(-x))
 
sigmoid_inputs = np.arange(-10,10,0.001)
sigmoid_outputs = sigmoid(sigmoid_inputs)
print("Sigmoid Function Input :: {}".format(sigmoid_inputs))
print("Sigmoid Function Output :: {}".format(sigmoid_outputs))
 
plt.plot(sigmoid_inputs,sigmoid_outputs)
plt.xlabel("Sigmoid Inputs")
plt.ylabel("Sigmoid Outputs")

plt.show()
