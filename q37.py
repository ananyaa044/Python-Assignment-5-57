# 37. Write a program to read a file and display only those lines that start with a particular character.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Apple\nBanana\nAvocado\nCherry\n")
character = input("Starting character: ")
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith(character):
            print(line, end="")
