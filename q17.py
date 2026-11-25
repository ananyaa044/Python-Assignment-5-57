# 17. Write a program to copy the contents of one text file into another file.
with open("source.txt", "w", encoding="utf-8") as file:
    file.write("These contents will be copied.\n")
with open("source.txt", "r", encoding="utf-8") as source:
    contents = source.read()
with open("copy.txt", "w", encoding="utf-8") as destination:
    destination.write(contents)
print("Contents copied to copy.txt")
