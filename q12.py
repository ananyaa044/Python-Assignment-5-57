# 12. Write a program to write five student names into a text file.
names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
with open("students.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")
print("Five student names written to students.txt")
