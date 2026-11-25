# 47. Write a program to check whether a specified path represents a file or directory.
import os

path = input("Enter a path: ")
if os.path.isfile(path):
    print("The path represents a file.")
elif os.path.isdir(path):
    print("The path represents a directory.")
else:
    print("The path does not exist.")
