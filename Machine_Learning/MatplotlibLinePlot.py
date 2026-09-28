import matplotlib.pyplot as plt

def main():

    X = [1,2,3,4,5]
    Y = [10,25,18,35,30]

    plt.plot(
        X,                           # Values of X axis
        Y,                           # Values of Y axis
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.grid(True) # Columns

    plt.legend() # Use to display the Names

    plt.show() # Show The Diagram which is Created on

if __name__ == "__main__":
    main()