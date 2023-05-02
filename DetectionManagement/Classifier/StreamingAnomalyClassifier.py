from DetectionManagement.ProvidedInterface.Model import Model

class StreamingAnomalyClassifier(Model):
    def determineAnomaly(self, data):
        print(f"determine based on {data} in streaming anomaly classifier")