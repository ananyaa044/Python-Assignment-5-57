# 50. Write a program to create a text file, write data into it, read its contents, close it and finally delete it.
import os

filename = "temporary_text.txt"
file = open(filename, "w", encoding="utf-8")
file.write("This text is written to a temporary file.\n")
file.close()
file = open(filename, "r", encoding="utf-8")
print(file.read(), end="")
file.close()
if os.path.exists(filename):
    os.remove(filename)
    print("Temporary file closed and deleted.")
