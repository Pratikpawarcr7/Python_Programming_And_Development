# Open file in read mode

fobj = open("Demo.txt", "r")

Count = 0

for Line in fobj:
    Count = Count + 1

fobj.close()

print("Total Lines:", Count)