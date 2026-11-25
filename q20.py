# 20. Write a program to store the first 100 natural numbers in a text file.
with open("natural_numbers.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(str(number) for number in range(1, 101)))
print("Numbers 1 to 100 saved to natural_numbers.txt")
