# 9. Write a program to display only those lines of a file that contain a particular word.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python is fun.\nFiles store data.\nPython reads files.\n")
word = input("Word to search for: ").casefold()
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        if word in line.casefold():
            print(line, end="")
