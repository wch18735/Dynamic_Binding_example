from DetectionManagement.ProvidedInterface.Model import Model

class SensorAnomalyClassifier(Model):
    def determineAnomaly(self, data):
        print(f"determine based on {data} in sensor anomaly classifier")

