# 27. Write a program to display the current file pointer position using tell().
with open("pointer.txt", "w+", encoding="utf-8") as file:
    file.write("Hello")
    print("Pointer after writing:", file.tell())
    file.seek(0)
    file.read(2)
    print("Pointer after reading 2 characters:", file.tell())
