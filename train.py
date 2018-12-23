import tensorflow as tf
from DataProcess import ExportData
import os
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):
    """
    Inspired by  不会停的蜗牛
    at https://www.jianshu.com/p/e112012a4b2d
    """

    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    Wx_plus_b = tf.matmul(inputs, Weights)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def train(startid, endid, fig=0):
    invec = tf.placeholder(dtype=tf.float32, shape=(1, 6))
    out = tf.placeholder(dtype=tf.float32)

    # layers
    hl1 = add_layer(inputs=invec, in_size=6, out_size=8, activation_function=tf.nn.tanh)
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

    plt.cla()
    for i in range(100):
        for j in range(startid, endid):
            train_data = ExportData(j)
            if train_data == 404:
                continue
            else:
                sess.run(trainer, feed_dict={invec: [train_data[0]], out: train_data[1]})
        plt.scatter(i, sess.run(prediction - out, feed_dict={invec: [train_data[0]], out: train_data[1]})[0][0],
                    c='red')

    tf.train.Saver().save(sess, r'./tf/train')
    writer = tf.summary.FileWriter(r'./tf/graph', sess.graph)

    if fig:
        plt.savefig('loss_process.png')
        print('误差变化图储存于 loss_process.png')


def lossdis(startid, n):
    if not os.path.exists(r'tf/train.index'):
        return 0

    invec = tf.placeholder(dtype=tf.float32, shape=(1, 6))
    out = tf.placeholder(dtype=tf.float32)

    # layers
    hl1 = add_layer(inputs=invec, in_size=6, out_size=8, activation_function=tf.nn.tanh)
    hl2 = add_layer(inputs=hl1, in_size=8, out_size=8, activation_function=tf.nn.tanh)
    prediction = add_layer(inputs=hl2, in_size=8, out_size=1)
    loss = tf.abs(out - prediction)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    tf.train.Saver().restore(sess, r'./tf/train')
    plt.cla()
    for i in range(startid, startid + n):
        train_data = ExportData(i)
        if train_data == 404:
            continue
        else:
            plt.scatter(i, sess.run(loss, feed_dict={invec: [train_data[0]], out: train_data[1]}), c='red')
    plt.savefig('loss_dis.png')
    print('误差变化图储存于 loss_diss.png')


def predict(aid):
    if not os.path.exists(r'tf/train.index'):
        return 0

    invec = tf.placeholder(dtype=tf.float32, shape=(1, 6))
    out = tf.placeholder(dtype=tf.float32)

    # layers
    hl1 = add_layer(inputs=invec, in_size=6, out_size=8, activation_function=tf.nn.tanh)
    hl2 = add_layer(inputs=hl1, in_size=8, out_size=8, activation_function=tf.nn.tanh)
    prediction = add_layer(inputs=hl2, in_size=8, out_size=1)
    loss = tf.abs(out - prediction)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    tf.train.Saver().restore(sess, r'./tf/train')
    vid_info = ExportData(aid)
    if vid_info == 404:
        return 404
    else:
        return sess.run(prediction, feed_dict={invec:[vid_info[0]]})


if __name__ == '__main__':
    while 1:
        inp = input('[T]：训练，[L]：检视误差，[P]预测一个视频的分数：')
        if 'T' == inp:
            startid = int(input('起始 id ：'))
            endid = int(input('终止 id ：'))
            lossfig = input('输出误差变化图？[Y]es or [N]o：')
            if lossfig == 'Y':
                lossfig = 1
            else: lossfig = 0
            train(startid, endid, lossfig)

        elif 'L' == inp:
            startid = int(input('从哪个视频 id 开始：'))
            n = int(input('看几个 id '))
            lossdis(startid, n)

        elif 'P' == inp:
            aid = int(input('视频 id：'))
            pre = predict(aid)
            if pre == 404:
                print('视频不存在')
            else:
                print(pre[0][0])
