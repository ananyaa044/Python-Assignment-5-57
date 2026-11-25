# 46. Write a program to display all filenames present in a specified directory.
import os

directory = input("Directory path (default: current directory): ") or "."
if os.path.isdir(directory):
    for name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, name)):
            print(name)
else:
    print("Directory does not exist.")
