# 45. Write a program to create a new directory using the os module.
import os

directory = "new_directory"
os.makedirs(directory, exist_ok=True)
print(f"Directory ready: {directory}")
