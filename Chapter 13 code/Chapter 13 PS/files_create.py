# Open 01_problem.py in read mode
with open("01_problem.py", "r") as file1:
    content1 = file1.read()  # Correct method to read file contents
    print("Contents of 01_problem.py:\n", content1)

# Open 02_problem.py in write mode (this will overwrite the file)
with open("02_problem.py", "w") as file2:
    file2.write("# This is 02_problem.py\n")

# Open 03_problem.py in append mode (this will add content without erasing existing data)
with open("03_problem.py", "a") as file3:
    file3.write("\n# Appended line in 03_problem.py\n")

print("Files have been processed successfully.")
