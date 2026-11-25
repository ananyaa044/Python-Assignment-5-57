# 18. Write a program to write student details such as name, roll number and marks into a file.
name = input("Student name: ")
roll_number = input("Roll number: ")
marks = input("Marks: ")
with open("student_details.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\nRoll number: {roll_number}\nMarks: {marks}\n")
print("Student details saved.")
