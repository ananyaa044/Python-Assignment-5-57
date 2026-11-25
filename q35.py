# 35. Write a program to search for a specific word in a file and display whether it exists.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python is useful for automation.")
word = input("Word to search for: ").casefold()
with open("sample.txt", "r", encoding="utf-8") as file:
    words = {token.strip(".,!?;:").casefold() for token in file.read().split()}
print("Word exists." if word in words else "Word does not exist.")
