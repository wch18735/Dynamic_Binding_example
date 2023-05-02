from abc import *

class DetectionManager(metaclass=ABCMeta):
    data = None
    detectionCriteria = None
    result = None

    def __init__(self):
        pass

    @abstractmethod
    def setData(self, data):
        pass

    @abstractmethod
    def loadModel(self, model):
        pass

    @abstractmethod
    def detectAnomaly(self):
        pass

    @abstractmethod
    def retrieveResult(self, data):
        pass