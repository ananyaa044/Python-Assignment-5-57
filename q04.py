# 4. Write a program to read a file line by line using the readline() function.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("First line\nSecond line\nThird line\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
