# 49. Write a program to rename a text file and then display its contents.
import os

old_name = "before_rename.txt"
new_name = "after_rename.txt"
with open(old_name, "w", encoding="utf-8") as file:
    file.write("Contents of the renamed text file.\n")
if os.path.exists(new_name):
    os.remove(new_name)
os.rename(old_name, new_name)
with open(new_name, "r", encoding="utf-8") as file:
    print(file.read(), end="")
