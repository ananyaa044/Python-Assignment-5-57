# 8. Write a program to count the total number of words in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python makes file handling easy.")
with open("sample.txt", "r", encoding="utf-8") as file:
    print("Total words:", len(file.read().split()))
