# 34. Write a program to count the occurrences of a particular word in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python is fun. Python is useful.")
word = input("Word to count: ").casefold()
with open("sample.txt", "r", encoding="utf-8") as file:
    words = file.read().casefold().split()
count = sum(token.strip(".,!?;:") == word for token in words)
print(f"'{word}' occurs {count} times.")
