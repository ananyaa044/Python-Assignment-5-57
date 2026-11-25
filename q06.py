# 6. Write a program to count the total number of characters in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    print("Total characters:", len(file.read()))
