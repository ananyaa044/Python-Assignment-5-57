# 44. Write a program to delete an existing file using the os module.
import os

filename = "delete_me.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("This sample file will be deleted.\n")
if os.path.exists(filename):
    os.remove(filename)
    print(f"Deleted {filename}.")
else:
    print("File does not exist.")
