import sys
import os
sys.path.append(os.pardir)  
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize=True, flatten=True, one_hot_label=False)

    return x_test, t_test
    

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    Z1 = sigmoid(a1)
    a2 = np.dot(Z1, W2) + b2
    Z2 = sigmoid(a2)
    a3 = np.dot(Z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
accuaracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)

    if p == t[i]:
        accuaracy_cnt += 1

print("Accuracy:" + str(float(accuaracy_cnt) / len(x)))

x, t = get_data()
network = init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']

print(x.shape)
print(t.shape)
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)