import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#==================================================================================================================================
# Step 3 : Decidede Independent and Dependent Variables
#==================================================================================================================================

print(Border)
print("Step 3 : Decidede Independent and Dependent Variables ")
print(Border)  

# X = Independent Variables / Features
# Y = Dependent Variables / Labels

features_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[features_cols]
Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#==================================================================================================================================
# Step 4 : Visualisation of Dataset
#==================================================================================================================================

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

# Scatter Plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()





