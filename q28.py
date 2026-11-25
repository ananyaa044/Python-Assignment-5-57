# 28. Write a program to change the file pointer position using seek().
with open("pointer.txt", "w+", encoding="utf-8") as file:
    file.write("ABCDEFGHIJ")
    file.seek(5)
    print("Pointer moved to:", file.tell())
    print("Remaining contents:", file.read())
