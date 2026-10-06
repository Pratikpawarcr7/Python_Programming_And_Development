import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Marvellous_Predictor():

    # Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables X : ",X)
    print("Values of Dependent Variables X : ",Y)


    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean_X is : ",mean_x)
    print("Mean_Y is : ",mean_y)

def main():
    Marvellous_Predictor()


if __name__ == "__main__":
    main()