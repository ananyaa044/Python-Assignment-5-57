# 13. Write a program to write multiple lines into a file using the writelines() function.
lines = ["Line one\n", "Line two\n", "Line three\n"]
with open("lines.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
print("Lines written to lines.txt")
