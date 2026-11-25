# 32. Write a program to count the number of uppercase and lowercase letters in a file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python FILE Handling")
with open("sample.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print("Uppercase letters:", sum(character.isupper() for character in contents))
print("Lowercase letters:", sum(character.islower() for character in contents))
