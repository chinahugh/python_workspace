import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
value = tf.constant(4, dtype=tf.float32)
print(tf._sys)
print(value)

