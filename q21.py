# 21. Write a program to demonstrate opening a file in read mode (r).
with open("mode_demo.txt", "w", encoding="utf-8") as file:
    file.write("This file is opened in read mode.\n")
with open("mode_demo.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")
