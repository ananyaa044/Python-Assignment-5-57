# 38. Write a program to read a text file and convert all lowercase letters into uppercase letters in another file.
with open("source.txt", "w", encoding="utf-8") as file:
    file.write("Convert these words to uppercase.\n")
with open("source.txt", "r", encoding="utf-8") as source:
    contents = source.read()
with open("uppercase.txt", "w", encoding="utf-8") as destination:
    destination.write(contents.upper())
print("Converted contents saved to uppercase.txt")
