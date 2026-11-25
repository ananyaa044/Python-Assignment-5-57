# 29. Write a program to read a file from a specified file pointer position.
with open("pointer.txt", "w", encoding="utf-8") as file:
    file.write("0123456789")
position = int(input("Start reading at character position (0-10): "))
with open("pointer.txt", "r", encoding="utf-8") as file:
    file.seek(position)
    print(file.read())
