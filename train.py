import tensorflow as tf
from DataProcess import ExportData
import os

def add_layer(inputs, in_size, out_size, activation_function=None):
    '''
    Inspired by  不会停的蜗牛
    at https://www.jianshu.com/p/e112012a4b2d
    '''

    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    Wx_plus_b = tf.matmul(inputs, Weights)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def train(startid, endid):
    invec = tf.placeholder(dtype=tf.float32, shape=(1,8))
    out = tf.placeholder(dtype=tf.float32)

    # layers
    hl1 = add_layer(inputs=invec, in_size=8, out_size=8, activation_function=tf.nn.tanh)
    hl2 = add_layer(inputs=hl1, in_size=8, out_size=8, activation_function=tf.nn.tanh)
    prediction = add_layer(inputs=hl2, in_size=8, out_size=1)
    loss = tf.abs(out - prediction)

    trainer = tf.train.RMSPropOptimizer(0.01).minimize(loss)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    if os.path.exists(r'tf/train.index'):
        tf.train.Saver().restore(sess, r'tf/train')
    else:
        pass

    for i in range(1000):
        for j in range(startid, endid):
            train_data = ExportData(j)
            if train_data == 404:
                continue
            else:
                sess.run(trainer, feed_dict={invec:[train_data[0]], out:train_data[1]})
        print(sess.run(prediction - out, feed_dict={invec:[train_data[0]], out:train_data[1]}))

    tf.train.Saver().save(sess, r'./tf/train')
    writer = tf.summary.FileWriter(r'./tf/graph', sess.graph)


if __name__ == '__main__':
    train(36676000, 36678336)
    os.system('pause')
