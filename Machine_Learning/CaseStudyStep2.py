import pandas as pd

Border = "="*70

#=================================================================================================================================
# Step 1 : Load the DataSet
#==================================================================================================================================

print(Border)
print(" Step 1 : Load the DataSet ")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded succefully")
print("Initial Entries from dataset are. : ")
print(df.head())


#==================================================================================================================================
# Step 2 : Data Analysis (EDA)
#==================================================================================================================================

print(Border)
print(" Step 2 : Data Analysis (EDA) ")
print(Border)  

print("Shape of dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing Values per Columns : ")
print(df.isnull().sum())

print("Class distribution (species count)")
print(df["species"].value_counts())

print("Statistical report of Dataset : ")
print(df.describe())






