import numpy as np
from Sigmoid import Sigmoid
from Activation import Activation


class Neuron:

    def __init__(self, name="", activ: Activation = Sigmoid()):
        self.w = np.matrix([1])
        self.prevs = np.array([])
        self.nexts = np.array([])
        self.name = name
        self.y = 0
        self.delta = 0
        self.activ = activ
        pass

    def addPrev(self, prev):
        self.prevs = np.append(self.prevs, prev)
        self.w = np.append(self.w, 1)
        prev.nexts = np.append(prev.nexts, self)
        pass

    def deltaCalc(self):
        pass

