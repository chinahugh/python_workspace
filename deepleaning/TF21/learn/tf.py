import tensorflow as tf
from matplotlib import pyplot as plt

m = tf.Variable(tf.constant(3, dtype=tf.float32))

lr = 0.9

point = []
counter = 100
for c in range(counter):
    with tf.GradientTape() as tape:
        loss = tf.square(m+1)
    dloss_dw = tape.gradient(loss, m)
    m.assign_sub(lr * dloss_dw)
    point.append(loss)
    print(loss)
    print("After %s epoch,w is %f,loss is %f" % (c, m.numpy(), loss))
plt.title("test")
plt.xlabel("m")
plt.ylabel("loss")
plt.plot([0, 2, 4, 6, 8], [0, 4, 8, 12, 16], "ro",label="asd")
plt.plot([0, 2, 4, 6, 8], [0, 4, 8, 12, 16],label="asd")
plt.legend()
plt.show()
