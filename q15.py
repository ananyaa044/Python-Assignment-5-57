# 15. Write a program to append additional text to an existing file.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Original text.\n")
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("This text was appended.\n")
print("Additional text appended to notes.txt")
