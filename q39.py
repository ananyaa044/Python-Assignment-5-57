# 39. Write a program to read a file and write its contents into another file in reverse character order.
with open("source.txt", "w", encoding="utf-8") as file:
    file.write("Python files")
with open("source.txt", "r", encoding="utf-8") as source:
    contents = source.read()
with open("reversed.txt", "w", encoding="utf-8") as destination:
    destination.write(contents[::-1])
print("Reversed contents saved to reversed.txt")
