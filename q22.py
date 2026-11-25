# 22. Write a program to demonstrate opening a file in write mode (w).
with open("write_mode.txt", "w", encoding="utf-8") as file:
    file.write("Write mode creates a file or replaces its contents.\n")
print("Data written to write_mode.txt")
