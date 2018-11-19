import tensorflow as tf

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


def main():
    invec = tf.placeholder(dtype=tf.int32, shape=(11))

    outvec =


if __name__ == '__main__':
    main()