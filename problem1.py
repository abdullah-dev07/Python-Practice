import copy

students = [
    ["Ali", [90, 80]],
    ["Sara", [85, 75]],
    ["John", [70, 60]]
]

students_shallow = copy.copy(students)

students_deep = copy.deepcopy(students)

students_shallow[0][1][0] = 100
students_deep[0][1][0] = 100

print(f"original list {students}")
print(f"shallow copy {students_shallow}")
print(f"deep copy {students_deep}")