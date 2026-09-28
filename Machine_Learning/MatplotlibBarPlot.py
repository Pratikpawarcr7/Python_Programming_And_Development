import matplotlib.pyplot as plt

def main():

    Language = ["C","C++","Java","Python"]

    Students = [30,40,35,55]

   
    plt.bar(
        Language,               # Values of X axis
        Students,               # Vaues of Y axis
        width=0.6,              # width of bars
        edgecolor = "black",    # border color of bars
        linewidth = 1,          # width of bar border
        alpha = 0.8,            # transperance 0.0 to 1.0
        label = "Students"      # legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Language")
    plt.ylabel("Students")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()