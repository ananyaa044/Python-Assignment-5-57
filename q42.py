# 42. Write a program to display the name and other available information of a file using appropriate file-related functions.
from pathlib import Path

path = Path(input("Enter a file path (default: sample.txt): ") or "sample.txt")
if path.is_file():
    info = path.stat()
    print("Name:", path.name)
    print("Suffix:", path.suffix)
    print("Size in bytes:", info.st_size)
    print("Last modified timestamp:", info.st_mtime)
else:
    print("File does not exist.")
