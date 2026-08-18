import os

Folder = input("Enter folder path: ")

for File in os.listdir(Folder):
    Path = os.path.join(Folder, File)

    if os.path.isfile(Path) and os.path.getsize(Path) == 0:
        os.remove(Path)
        print("Deleted:", File)

print("Automation completed!")