# 7. Write a program to count the total number of lines in a text file.
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("One\nTwo\nThree\n")
with open("sample.txt", "r", encoding="utf-8") as file:
    print("Total lines:", len(file.readlines()))
