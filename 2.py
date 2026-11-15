# CREATE
students = ("Rahul", "Amit", "Priya")

# READ
print("First student:", students[0])

# INSERT AT INDEX
temp = list(students)
temp.insert(1, "Vikas")
students = tuple(temp)

# UPDATE
temp = list(students)
temp[2] = "Neha"
students = tuple(temp)

# DELETE
temp = list(students)
del temp[0]
students = tuple(temp)

# PRINT USING LOOP
print("All students:")
for student in students:
    print(student)