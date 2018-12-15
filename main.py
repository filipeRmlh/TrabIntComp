from Neuron import Neuron
from Sigmoid import Sigmoid

neuron = Neuron("N1", Sigmoid())
neuron2 = Neuron("N2", Sigmoid())
neuron.addPrev(neuron2)
