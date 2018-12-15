import abc


class Activation(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fn(self, s):
        return s > 0

    @abc.abstractmethod
    def dfn(self, s):
        return 0
