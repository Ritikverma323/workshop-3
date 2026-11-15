# CREATE
students = {
    "Rahul": 80,
    "Amit": 70,
    "Priya": 90
}

# READ
print("Rahul's marks:", students["Rahul"])

# INSERT AT POSITION 1
items = list(students.items())
items.insert(1, ("Vikas", 85))
students = dict(items)

# UPDATE
students["Amit"] = 95

# DELETE
del students["Priya"]

# PRINT USING LOOP
print("All students:")
for name, marks in students.items():
    print(name, marks)