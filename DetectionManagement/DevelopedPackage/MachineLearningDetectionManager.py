from DetectionManagement.ProvidedInterface.DetectionManager import DetectionManager

class MachineLearningDetectionManager(DetectionManager):
    def __init__(self):
        pass

    def loadModel(self, model):
        self.detectionCriteria = model

    def setData(self, data):
        self.data = data

    def detectAnomaly(self):
        if self.detectionCriteria == None:
            print("None")
        else:
            self.detectionCriteria.determineAnomaly(self.data)

    def retrieveResult(self):
        return 0

