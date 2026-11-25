# 3. Write a program to read only the first 10 characters from a file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python file handling")
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read(10))
