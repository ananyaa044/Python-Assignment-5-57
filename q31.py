# 31. Write a program to count the number of vowels in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python programming")
with open("sample.txt", "r", encoding="utf-8") as file:
    contents = file.read().casefold()
print("Vowels:", sum(character in "aeiou" for character in contents))
