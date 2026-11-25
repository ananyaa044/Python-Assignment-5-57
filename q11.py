# 11. Write a program to create a new text file and write a welcome message into it.
with open("welcome.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to Python programming!\n")
print("Welcome message written to welcome.txt")
