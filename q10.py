# 10. Write a program to display the contents of a file in reverse order of lines.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("First\nSecond\nThird\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in reversed(file.readlines()):
        print(line, end="")
