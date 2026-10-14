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

    df = df.drop(
        ["Passengerid", "zero", "name"],
        axis=1,
        errors="ignore"
    )

    # Replace blank spaces with NaN
    df = df.replace(r"^\s*$", np.nan, regex=True)

    # Convert columns to numeric
    NumericColumns = [
        "Age", "Fare", "Sex", "sibsp",
        "Parch", "Pclass", "Embarked", "Survived"
    ]

    for col in NumericColumns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Fill missing values in feature columns
    for col in df.columns:
        if col != "Survived":
            if df[col].isnull().any():
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col] = df[col].fillna(df[col].median())
                else:
                    df[col] = df[col].fillna(
                        df[col].mode()[0]
                    )

    # Remove rows with missing target values
    df = df.dropna(subset=["Survived"])

    # Convert any remaining categorical columns
    df = pd.get_dummies(
        df,
        columns=df.select_dtypes(include="object").columns.tolist(),
        drop_first=True,
        dtype=int
    )

    print(df.head())
    print("Data preprocessing completed successfully")

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

# Step 4 : Train the model

#-----------------------------------------------------
#   Function Name : TrainModel
#   Description :   It performs model training
#   Input :         Training fetures and labels
#   Output :        Trained model
#   Author :        Pratik Ravindra Pawar
#   Date :          16/08/2026
#-----------------------------------------------------

def TrainModel(X_train, Y_train):

    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train, Y_train)

    print(" Model Train Successfully : ")

    return model
# Step 5 : Evaluate model

#-----------------------------------------------------
#   Function Name : EvaluateModel
#   Description :   It performs model testing
#   Input :         model, testing data (fetures ,labels)
#   Output :        none
#   Author :        Pratik Pawar
#   Date :          16/08/2026
#-----------------------------------------------------

def EvaluateModel(model,X_test,Y_test):

    Y_pred = model.predict(X_test)

    accurancy = accuracy_score(Y_test,Y_pred)

    print("Accurency : ",accurancy)

    print(confusion_matrix(Y_test,Y_pred))
# Step 6 : Preserve Model

#-----------------------------------------------------
#   Function Name : PreserveModel
#   Description :   It performs model preservation into .pkl file
#   Input :         model
#   Output :        none
#   Author :        Piyush Manohar Khairnar
#   Date :          16/08/2026
#-----------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved with name : ",filename)
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

    # Step 4 : 
    model = TrainModel(X_train, Y_train)

    # Step 5 : 
    EvaluateModel(model,X_test,Y_test)

if __name__ == "__main__":
    main()