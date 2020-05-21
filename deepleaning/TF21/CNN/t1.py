import tensorflow as tf
from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np

# 导入数据
x_data = datasets.load_iris().data
y_data = datasets.load_iris().target

np.random.seed(116)  # 使用相同的seed，保证输入特征和标签一一对应
np.random.shuffle(x_data)
np.random.seed(116)
np.random.shuffle(y_data)
tf.random.set_seed(116)

x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]

x_train = tf.cast(x_train, tf.float32)
x_test = tf.cast(x_test, tf.float32)

train_map = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_map = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

w = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))
b = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))

lr = 0.1
loss_all = 0
epochs = 120
for _ in range(1):
    for epoch in range(epochs):
        xi = x_train[epoch:epoch+1]
        yi = y_train[epoch:epoch+1]
        print("xi {}, y_: {}".format(xi, yi))
        with tf.GradientTape() as tape:
            jy = tf.argmax(tf.matmul(xi,w) + b)
            jjy = tf.nn.softmax(jy)
            y = tf.one_hot(jjy, depth=3)
            loss = tf.reduce_mean(tf.square(yi - y))            
        grads = tape.gradient(loss, [w, b])
        w.assign_sub(lr * grads[0])
        b.assign_sub(lr * grads[1])
        print("y {}, y_: {}".format(y, yi))
        print("Epoch {}, loss: {}".format(epoch, loss))
        plt.plot(epoch, loss, "r*", label="asd")
pass
print("w:{},b:{}".format(w, b))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
