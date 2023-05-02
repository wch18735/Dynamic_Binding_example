from abc import *

class Model(metaclass=ABCMeta):
    @abstractmethod
    def determineAnomaly(self, data):
        pass