# 48. Write a program to demonstrate the use of os.path.exists() and os.path.getsize().
import os

filename = "size_demo.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("Check this file's size.")
if os.path.exists(filename):
    print("File exists.")
    print("File size:", os.path.getsize(filename), "bytes")
else:
    print("File does not exist.")
