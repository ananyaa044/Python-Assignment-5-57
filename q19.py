# 19. Write a program to store the multiplication table of a given number in a text file.
number = int(input("Enter a number: "))
with open("multiplication_table.txt", "w", encoding="utf-8") as file:
    for multiplier in range(1, 11):
        file.write(f"{number} x {multiplier} = {number * multiplier}\n")
print("Table saved to multiplication_table.txt")
