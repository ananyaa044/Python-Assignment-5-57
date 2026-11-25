# 26. Write a program to demonstrate opening a file in append and read mode (a+).
with open("aplus.txt", "w", encoding="utf-8") as file:
    file.write("Existing text.\n")
with open("aplus.txt", "a+", encoding="utf-8") as file:
    file.write("Appended text.\n")
    file.seek(0)
    print(file.read(), end="")
