from DetectionManagement.ProvidedInterface.Model import Model

class TestAnomalyClassifier(Model):
    def determineAnomaly(self, data):
        print(f"determine based on {data} in test anomaly classifier")