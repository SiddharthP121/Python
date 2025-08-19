'''
You are designing a Library system.

The library has a shared fine rate for overdue books (fine_per_day), which is the same for all members.

Each member has their own name and books_borrowed count.

Requirements:

Create a LibraryMember class with:

Class attribute: fine_per_day (default ₹5)

Instance attributes: name and books_borrowed

Add a method change_fine_rate(new_rate) as a class method to update the fine rate for all members.

Add a method borrow_book(count) to increase the member's books_borrowed.

Add a method calculate_fine(days_overdue) that calculates fine using:

Instance's own fine_per_day if it exists.

Otherwise, use the class attribute.
'''

class LibraryMember:
    fine_per_day = 5
    def __init__(self, name, books_borrowed):
        self.name = name
        self.books_borrowed = books_borrowed
    @classmethod
    def change_fine_rate(cls, new_rate):
        LibraryMember.fine_per_day = new_rate
    def borrow_book(self, count):
        self.books_borrowed += count 
        return self.books_borrowed
    def calculate_fine(self, days_overdue):
        if 'fine_per_day' in self.__dict__:
            return self.fine_per_day * days_overdue
        else:
            fine = days_overdue * LibraryMember.fine_per_day
            return fine


member1 = LibraryMember('Siddharth', 0)
member2 = LibraryMember('Shikhar', 2)

print('Books Borrowed',member1.borrow_book(1))
print('Fine' ,member1.calculate_fine(4))
print('Books Borrowed',member2.borrow_book(1))
print('Fine' ,member2.calculate_fine(4))

print(member1.__dict__)

print('The fine per day is', LibraryMember.fine_per_day)
LibraryMember.change_fine_rate(15)
print('The fine per day is', LibraryMember.fine_per_day)

print('Books Borrowed',member1.borrow_book(1))
print('Fine' ,member1.calculate_fine(4))
print('Books Borrowed',member2.borrow_book(1))
print('Fine' ,member2.calculate_fine(4))

member3 = LibraryMember('Anshul', 3)

member3.fine_per_day = 30

print(member3.__dict__)
print('Books Borrowed', member3.borrow_book(1))
print('Fine' ,member3.calculate_fine(7))
