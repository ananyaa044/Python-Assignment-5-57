# 33. Write a program to count the number of digits and special characters in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Room 204: A+B!")
with open("sample.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print("Digits:", sum(character.isdigit() for character in contents))
print("Special characters:", sum(not character.isalnum() and not character.isspace() for character in contents))
