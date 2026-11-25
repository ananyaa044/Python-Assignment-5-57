# 14. Write a program to accept text from the user and store it in a file.
text = input("Enter text to save: ")
with open("user_text.txt", "w", encoding="utf-8") as file:
    file.write(text + "\n")
print("Text saved to user_text.txt")
