# CREATE
students = ["Rahul", "Amit", "Priya"]

# READ
print("First student:", students[0])

# INSERT AT INDEX
students.insert(1, "Vikas")

# UPDATE
students[2] = "Neha"

# DELETE
del students[0]

# PRINT USING LOOP
print("All students:")
for student in students:
    print(student)