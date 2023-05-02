from DetectionManagement.DevelopedPackage.MachineLearningDetectionManager import MachineLearningDetectionManager
from DetectionManagement.ImportManager.ImportManager import ImportManager

if __name__=="__main__":
    m = MachineLearningDetectionManager()

    # Data
    m.setData("Sample Data")

    # Import Manager
    ima = ImportManager()

    while True:
        ima.load_module()

        print(f"0. refresh")
        for i, m_name in enumerate(ima.classes):
            print(f"{i+1}. {m_name}")

        command = int(input())
        if command == 0:
            continue
        else:
            model = ima.retrieve_classifier(command)
            m.loadModel(model)
            m.detectAnomaly()


