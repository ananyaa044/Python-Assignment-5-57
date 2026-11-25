# 41. Write a program to check whether a specified file exists using standard file-related functions.
from pathlib import Path

path = Path(input("Enter a file path (default: sample.txt): ") or "sample.txt")
print("File exists." if path.is_file() else "File does not exist.")
