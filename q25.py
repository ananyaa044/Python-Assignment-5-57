# 25. Write a program to demonstrate opening a file in write and read mode (w+).
with open("wplus.txt", "w+", encoding="utf-8") as file:
    file.write("Written using w+ mode.")
    file.seek(0)
    print(file.read())
