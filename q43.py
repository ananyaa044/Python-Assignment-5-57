# 43. Write a program to rename an existing file using the os module.
import os

old_name = "old_name.txt"
new_name = "new_name.txt"
with open(old_name, "w", encoding="utf-8") as file:
    file.write("This file will be renamed.\n")
if os.path.exists(new_name):
    os.remove(new_name)
os.rename(old_name, new_name)
print(f"Renamed {old_name} to {new_name}.")
