import pandas as pd
import numpy as np
import joblib # Model Presev Krnay Sathi 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Step 1 : Load the Data

#---------------------------------------------------------------------------------
# Function Name  :  Load the Data
# Description    :  Load the Data from CSV
# Input          :  Name of CSV file
# OutPut         :  Data Frame
# Authore        :  Pawar Pratik Ravindra
# Date           :  16 / 08 / 2026
#---------------------------------------------------------------------------------
def LoadData(filename):

    df = pd.read_csv(filename)

    print("Dataset loaded successfully")
    print(df.head())

    return df

# Step 2 : Data Preprocessing

#---------------------------------------------------------------------------------
# Function Name  :  Preprocessing
# Description    :  It Perform Data analysis
# Input          :  Data Frame
# OutPut         :  Updated Data Frame
# Authore        :  Pawar Pratik Ravindra
# Date           :  16 / 08 / 2026
#---------------------------------------------------------------------------------
def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors = "ignore"
    )

    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert categorical to numeric data     
    df = pd.get_dummies(
        df,  
        columns=["Embarked"],
        drop_first= True,
        dtype=int
    )

    print(df.head())

    print("Data prepsocessing completed")

    return df 
# Step 3 : Split Data 

#-----------------------------------------------------
#   Function Name : SplitData
#   Description :   It performs Splitting activity
#   Input :         Data Frame
#   Output :        4 subsets for traiing and testing
#   Author :        Piyush Manohar Khairnar
#   Date :          16/08/2026
#-----------------------------------------------------
def SplitData(df):

    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
        )

    print("Dataset Splitting completed Successfully")

    return X_train,X_test,Y_train,Y_test


#---------------------------------------------------------------------------------
# Function Name  :  Main
# Description    :  Entry point function
# Input          :  None
# OutPut         :  None
# Authore        :  Pawar Pratik Ravindra
# Date           :  16 / 08 / 2026
#---------------------------------------------------------------------------------    
def main():

    # Step 1    
    
    df = LoadData("MarvellousTitanicDataset.csv")

    # Step 2
    
    df = PreprocessData(df)

    # Step 3_

    X_train,X_test,Y_train,Y_test = SplitData(df)

if __name__ == "__main__":
    main()