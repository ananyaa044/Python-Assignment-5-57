# 24. Write a program to demonstrate opening a file in read and write mode (r+).
with open("rplus.txt", "w", encoding="utf-8") as file:
    file.write("Original text")
with open("rplus.txt", "r+", encoding="utf-8") as file:
    print("Before:", file.read())
    file.seek(0)
    file.write("Updated")
    file.seek(0)
    print("After:", file.read())
