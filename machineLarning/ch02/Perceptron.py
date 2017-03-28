import numpy as np


class Perceptron(object):
    """ パーセプトロンの分類機

    パラメータ
    eta : float
        学習率(0.0より大きく1.0以下の値)
    
    n_iter : int
        トレーニングデータのトレーニング回数

    属性
    ---------------------------
    w_ :  1次元配列
        適合後の重み

    errors_ : リスト
        各エポックでの誤分類機
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    
    def fit(self, x, y):

        """ トレーニングデータに適合させる

        パラメータ

        ---------

        x : {配列のようなデータ構造}, shape = [n_samples, n_features]
            トレーニングデータ

            n_sampleはサンプルの個数、n_featureは特微量の個数

        y : 配列のようなデータ構造, shape = [n_samples]
            目的変数

         戻り値

         -----------

         self : object

