# 40. Write a program to merge the contents of two text files into a third file.
with open("first.txt", "w", encoding="utf-8") as file:
    file.write("Contents of the first file.\n")
with open("second.txt", "w", encoding="utf-8") as file:
    file.write("Contents of the second file.\n")
with open("first.txt", "r", encoding="utf-8") as first:
    first_contents = first.read()
with open("second.txt", "r", encoding="utf-8") as second:
    second_contents = second.read()
with open("merged.txt", "w", encoding="utf-8") as merged:
    merged.write(first_contents + second_contents)
print("Files merged into merged.txt")
