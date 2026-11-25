# 2. Write a program to read the entire contents of a file using the read() function.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Reading the complete contents of this file.\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print(contents, end="")
