'''
A university system has the following requirements:

Person (Base Class)

Attribute: name

Method: show_details() → prints "Person: <name>"

Employee (inherits from Person)

Attribute: salary

Method: show_details() → prints "Employee: <name>, Salary: <salary>"

Student (inherits from Person)

Attribute: roll_no

Method: show_details() → prints "Student: <name>, Roll No: <roll_no>"

ResearchScholar (inherits from both Employee and Student → Hybrid Inheritance)

Attribute: field

Method: show_details() → should print:
"Research Scholar: <name>, Roll No: <roll_no>, Salary: <salary>, Field: <field>"

Write a Python program to implement this structure.
Create an object of ResearchScholar and demonstrate:

Method Overriding

Use of super()

MRO (Method Resolution Order).
'''

class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs) #optional where the parent class is <object>
        self.name = name
    
class Employee(Person):
    def __init__(self, salary, **kwargs):
        super().__init__(**kwargs)
        self.salary = salary
   

class Student(Person):
    def __init__(self, roll_no, **kwargs):
        super().__init__(**kwargs)
        self.roll_no = roll_no
    

class Research_scholer(Student, Employee):
    def __init__(self, name, roll_no, salary, field, **kwargs):
        super().__init__(name = name, roll_no = roll_no, salary = salary)
        self.field = field
    def show_details(self):
        print(
            f"Research Scholar: {self.name}, "
            f"Roll No: {self.roll_no}, "
            f"Salary: {self.salary}, "
            f"Field: {self.field}"
        )


s4 = Research_scholer('Shikhar', 1000, 78000, 'Computer')
s4.show_details()

