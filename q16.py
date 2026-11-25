# 16. Write a program to demonstrate the difference between write mode and append mode.
with open("modes.txt", "w", encoding="utf-8") as file:
    file.write("This replaces previous contents.\n")
with open("modes.txt", "a", encoding="utf-8") as file:
    file.write("This is added at the end.\n")
with open("modes.txt", "r", encoding="utf-8") as file:
    print(file.read(), end="")
