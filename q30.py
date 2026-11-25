# 30. Write a program to demonstrate the use of close() and check whether a file is closed.
file = open("close_demo.txt", "w", encoding="utf-8")
file.write("A short example.")
file.close()
print("Is file closed?", file.closed)
