# 23. Write a program to demonstrate opening a file in append mode (a).
with open("append_mode.txt", "w", encoding="utf-8") as file:
    file.write("Existing content.\n")
with open("append_mode.txt", "a", encoding="utf-8") as file:
    file.write("New content appended.\n")
print("Data appended to append_mode.txt")
