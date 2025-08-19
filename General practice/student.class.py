class StudentInfo:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def add_marks(self):
        sub_name = input('Enter the subject name to update the marks\n').lower()
        if sub_name in marks:
            sub_mark = int(input(f'Enter the {sub_name} mark to update the marks\n'))
            self.marks[sub_name] = sub_mark if sub_mark < 100 and sub_mark > 0 else print('Invalid marks')
            return self.marks
        else:
            print('Invalid subject name\n')
    def average(self):
        total = sum(self.marks.values())  
        average = total/5
        return average

    def grade(self):
        average_marks = float(self.average())
        if average_marks >= 80 and average_marks < 100:
            return 'A'
        elif average_marks >= 60 and average_marks < 79:
            return 'B'
        elif average_marks >= 40 and average_marks < 59:
            return 'C'
        else:
            return 'Fail'
    def details(self):
        print(f'Name = {self.name}')
        print(f'Marks: \n {self.marks} ')


name = input('Enter student name\n')
marks = {
    'maths' : 0,
    'computer': 0,
    'english' : 0,
    'hindi': 0,
    'science' : 0,
}

student = StudentInfo(name, marks)


while True:
    choice = int(input('Enter 1 for adding or updating marks\n Enter 2 for average\n Enter 3 for grade\n Enter 4 for details\n Enter 5 to exit\n'))

    if choice == 1:
        print(student.add_marks())
    elif choice == 2:
        print(student.average())
    elif choice == 3:
        print(student.grade())
    elif choice == 4:
        print(student.details())
    elif choice == 4:
        break
    else:
        print("Invalid input\n")
