import importlib
from pathlib import Path
import os

class ImportManager:
    plugin_path = "./DetectionManagement/Classifier"
    classes = None

    def load_module(self):
        self.classes = [x.split(".")[0] for x in os.listdir(self.plugin_path) if x != "__pycache__"]
        return self.classes

    def retrieve_classifier(self, idx):
        module = importlib.import_module(f"DetectionManagement.Classifier.{self.classes[idx - 1]}")
        clazz = getattr(module, self.classes[idx - 1])
        return clazz()

