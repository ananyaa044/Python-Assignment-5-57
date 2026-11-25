# 5. Write a program to read all lines of a file using the readlines() function.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.writelines(["First line\n", "Second line\n", "Third line\n"])
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    print(line, end="")
