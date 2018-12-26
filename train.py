import tensorflow as tf
from DataProcess import ExportData
import os
import matplotlib.pyplot as plt


def train(startid, endid, fig=0):
    invec = tf.placeholder(dtype=tf.float32, shape=(1, 6), name='invec')
    out = tf.placeholder(dtype=tf.float32, name='out')

    # layers
    weights1 = tf.Variable(tf.random_normal([6, 6]), name='w1')
    offset1 = tf.Variable(0., name='b1')
    hl1 = tf.nn.tanh(tf.matmul(invec, weights1) + offset1)
    weights2 = tf.Variable(tf.random_normal([6, 6]), name='w2')
    offset2 = tf.Variable(0., name='b2')
    hl2 = tf.nn.tanh(tf.matmul(hl1, weights2) + offset2)
    weights_pre = tf.Variable(tf.random_normal([6, 1]), name='w_pre')
    offset_pre = tf.Variable(0., name='b_pre')
    prediction = tf.matmul(hl2, weights_pre) + offset_pre
    loss = tf.sqrt(tf.abs(out - prediction))

    trainer = tf.train.RMSPropOptimizer(0.01).minimize(loss)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    if os.path.exists(r'tf/train.index'):
        tf.train.Saver().restore(sess, save_path="./tf/train")
    else:
        pass

    saver = tf.train.Saver(max_to_keep=4)
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
        saver.save(sess, r'./tf/train')

    if fig:
        plt.savefig('loss_process.png')
        print('误差变化图储存于 loss_process.png')


def lossdis(startid, n):
    if not os.path.exists(r'tf/train.index'):
        raise FileNotFoundError('Model not found.')

    invec = tf.placeholder(dtype=tf.float32, shape=(1, 6), name='invec')
    out = tf.placeholder(dtype=tf.float32, name='out')

    # layers
    weights1 = tf.Variable(tf.random_normal([6, 6]), name='w1')
    offset1 = tf.Variable(0., name='b1')
    hl1 = tf.nn.tanh(tf.matmul(invec, weights1) + offset1)
    weights2 = tf.Variable(tf.random_normal([6, 6]), name='w2')
    offset2 = tf.Variable(0., name='b2')
    hl2 = tf.nn.tanh(tf.matmul(hl1, weights2) + offset2)
    weights_pre = tf.Variable(tf.random_normal([6, 1]), name='w_pre')
    offset_pre = tf.Variable(0., name='b_pre')
    prediction = tf.matmul(hl2, weights_pre) + offset_pre
    loss = tf.sqrt(tf.abs(out - prediction))

    trainer = tf.train.RMSPropOptimizer(0.01).minimize(loss)
    sess = tf.Session()

    tf.train.Saver().restore(sess, save_path="./tf/train")

    plt.cla()
    for i in range(startid, startid + n):
        train_data = ExportData(i)
        if train_data == 404:
            continue
        else:
            plt.scatter(i, sess.run(out - prediction, feed_dict={invec: [train_data[0]], out: train_data[1]}), c='red',
                        s=2500 / n)
    plt.savefig('loss_dis.png')
    print('误差分布图储存于 loss_dis.png')


def predict(aid):
    if not os.path.exists(r'tf/train.index'):
        raise FileNotFoundError('Model not found.')

    invec = tf.placeholder(dtype=tf.float32, shape=(1, 6), name='invec')
    out = tf.placeholder(dtype=tf.float32, name='out')

    # layers
    weights1 = tf.Variable(tf.random_normal([6, 6]), name='w1')
    offset1 = tf.Variable(0., name='b1')
    hl1 = tf.nn.tanh(tf.matmul(invec, weights1) + offset1)
    weights2 = tf.Variable(tf.random_normal([6, 6]), name='w2')
    offset2 = tf.Variable(0., name='b2')
    hl2 = tf.nn.tanh(tf.matmul(hl1, weights2) + offset2)
    weights_pre = tf.Variable(tf.random_normal([6, 1]), name='w_pre')
    offset_pre = tf.Variable(0., name='b_pre')
    prediction = tf.matmul(hl2, weights_pre) + offset_pre
    loss = tf.sqrt(tf.abs(out - prediction))

    trainer = tf.train.RMSPropOptimizer(0.01).minimize(loss)
    sess = tf.Session()

    tf.train.Saver().restore(sess, save_path="./tf/train")

    vid_info = ExportData(aid)
    if vid_info == 404:
        return 404
    else:
        return sess.run(prediction, feed_dict={invec: [vid_info[0]]})


if __name__ == '__main__':
    while 1:
        inp = input('[T]：训练（以一段编号范围的视频为材料）\n[L]：检视一段编号范围内的误差\n[P]：预测一个视频的分数\n：')
        if 'T' == inp:
            startid = int(input('训练起始 id ：'))
            endid = int(input('终止 id ：'))
            lossfig = input('输出误差变化图？[Y]es or [N]o：')
            if lossfig == 'Y':
                lossfig = 1
            else:
                lossfig = 0
            train(startid, endid, lossfig)

        elif 'L' == inp:
            startid = int(input('检视起始 id ：'))
            n = int(input('看几个 id：'))
            lossdis(startid, n)

        elif 'P' == inp:
            aid = int(input('视频 id：'))
            pre = predict(aid)
            if pre == 404:
                print('视频不存在')
            else:
                print(pre[0][0])
