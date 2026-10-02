import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    border = "="*40

    print(border)
    print("Step 1 : Load the DataSet From CSV File")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some Entries from dataset : ")
    print(df.head())
    print(border)


def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()