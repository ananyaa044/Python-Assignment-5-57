path = "sample.txt"
with open(path, "w", encoding="utf-8") as file:
    file.write("Welcome to Python file handling!\nThis is a sample text file.\n")

# 1. Write a Python program to open an existing text file in read mode and display its contents.
with open(path, "r", encoding="utf-8") as file:
    print(file.read(), end="")
