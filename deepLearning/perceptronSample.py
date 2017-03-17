import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2

    if tmp <= theta:
        return 0
    else:
        return 1


print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

x = np.array([0, 1]) 
w = np.array([0.5, 0.5]) 
b = -0.7
print(w*x)

print(np.sum(w*x))

print(np.sum(w*x) + b)


def AND2(x1, x2):
    '''ANDを実装'''
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b

    if(tmp <= 0):
        return 0
    else:
        return 1


print(AND2(0, 0))
print(AND2(0, 1))
print(AND2(1, 0))
print(AND2(1, 1))


def NAND(x1, x2):
    ''' NANDを実装'''
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b

    if(tmp <= 0):
        return 0
    else:
        return 1


print('NAND')
print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))


def OR(x1, x2):
    ''' ORを実装'''
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b

    if(tmp <= 0):
        return 0
    else:
        return 1


print('OR')
print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))


def XOR(x1, x2):
    ''' XORを実装 '''
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print('XOR')
print(XOR(0, 0))
print(OR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))