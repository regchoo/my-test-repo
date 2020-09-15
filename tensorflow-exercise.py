import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
## import numpy as np

## data=np.random.randint(10, size=100)

x = tf.Variable(0, name='x')
## x = tf.constant(data, name='x')
## y = tf.Variable((5*x**2-3*x+15), name='y')

model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    for i in range(5):
        x = x+1
        print(session.run(x))
