# 36. Write a program to find the longest word in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python file handling is straightforward.")
with open("sample.txt", "r", encoding="utf-8") as file:
    words = [word.strip(".,!?;:") for word in file.read().split()]
longest = max(words, key=len, default="")
print("Longest word:", longest)
