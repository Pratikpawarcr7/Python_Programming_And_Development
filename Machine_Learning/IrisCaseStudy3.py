from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    Dataset = load_iris()

    # Meta of the Dataset

    print("Indipendent Variables Are : ")
    print(Dataset.feature_names)
    print("Length of Independent Variable",len(Dataset.feature_names))

    print("Dipendent Variables Are : ")
    print(Dataset.target_names) 
    print("Length of Dependent Variable",len(Dataset.target_names))

if __name__ == "__main__":
    main()