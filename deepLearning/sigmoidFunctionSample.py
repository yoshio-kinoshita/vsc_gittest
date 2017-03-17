
import numpy as np
import matplotlib.pylab as plt

''' シグモイド関数サンプル'''
# def step_function(x):
#    if x > 0:
#        return 1
#    else:
#        return 0


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.array([-1.0, 1.0, 2.0])
print(x)

y = x > 0
print(y)

y = y.astype(np.int)
print(y)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
# y軸の範囲指定
plt.ylim(-0.1, 1.1)
plt.show()


def sigmoid(x):
    ''' シグモイド関数 '''
    return 1 / (1 + np.exp(-x))


x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))


t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)

print(1.0 / t)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()