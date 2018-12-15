import numpy as np
from Activation import Activation


class Sigmoid(Activation):
    def __init__(self):
        pass

    def fn(self, z):
        return 1 / (1 + np.exp(-z))

    def dfn(self, z):
        return self.fn(z)*(1-self.fn(z))
