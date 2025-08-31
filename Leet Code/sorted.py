data = [5, 2, 9, 1, 7]

print("Accending --> ",sorted(data, key = lambda x: x))
print("Decending --> ",sorted(data, key = lambda x: x, reverse = True))

students = [("Komal", 22), ("Hemlata", 21), ("Nisha", 28)]

print("Sorted by name --> ", sorted(students, key=lambda x : x[0]))
print("Sorted by age --> ", sorted(students, key=lambda x : x[1]))
