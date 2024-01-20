#!/usr/bin/env python

file_name = "exmaple.txt"

with open(file_name, "w") as file:
    file.write("Hello, this is some content written to the file.\n")
    file.write("You can write more lines like this.")
    file.write("This is a new Line")
    file.mode = "000"

for i in range(5):
    print(i)
