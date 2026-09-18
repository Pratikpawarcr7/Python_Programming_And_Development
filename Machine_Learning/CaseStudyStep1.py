import pandas as pd

Border = "-"*30

###########################################################
# Step 1 : Load the DataSet
###########################################################

print(Border)
print(" Step 1 : Load the DataSet ")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)  # df = datafram

print("Dataset loaded succefully")
print("Initial Entries from dataset are. : ")
print(df.head())

