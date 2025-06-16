import copy


class Student:
    @staticmethod
    def decorator(func):
        def wrapper(self, name, age, grades):
            print("New student created!")
            print(f"Name: {name} \n")
            print(f"Age: {age} \n")
            print(f"Grades: {grades} \n")
            func(self, name, age, grades)
        return wrapper    


    @decorator

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def save_data(self):
        file = open("student_data.txt","a")
        std_data = self.name + "," + str(self.age) + "," + " ".join(self.grades) + "\n"
        file.write(std_data)
        file.close()
        print("student data saved!!")

    def load_data(self):
        file = open("student_data.txt", 'r')
        for line in file:
            print(line)   


    def __str__(self):
        return f"Name: {self.name}, Age: {str(self.age)}, Grades: {self.grades}"



class StudentFileIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')


    def __iter__(self):
        return self
    
    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration

        parsed_line = line.strip().split(',')
        name = parsed_line[0]
        age = parsed_line[1]
        grades = parsed_line[2].strip().split()
        return name,age,grades



std_iterator = StudentFileIterator('student_data.txt')

student_list = []

for student in std_iterator:
    # print(student)
    student_list.append(student)


student_list_backup = copy.deepcopy(student_list)
student_list.append(('ahmed', '22', ['A', 'B']))



print("Original student list\n")
for student in student_list:
    print(student)

print("----------\n\n")


print("Backup student list\n\n")

for student in student_list_backup:
    print(student)

# abd = Student("abdullah", 23, ['A','B'])
# ahmed = Student("ahmed", 22, ['A','B'])


# ahmed.save_data()
