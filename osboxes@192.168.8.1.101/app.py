#!/usr/bin/env python3

file_name = "example.txt"

with open(file_name, "w") as file:
    file.write("Hello, this is some content written to the file.\n")
    file.write("You can write more lines like this.")

print(f"File '{file_name}' has been created.")
