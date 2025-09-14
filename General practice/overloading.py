'''
create a Rectangle class and overload the comparison operators to compare the areas
#of two rectangles.
# __eq__(self, other): Equality (==)
#● __lt__(self, other): Less than (<)
#● __le__(self, other): Less than or equal (<=)
#● __gt__(self, other): Greater than (>)
#● __ge__(self, other): Greater than or equal (>=)
'''

class Rectangle():
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def __eq__(self, other):
        return self.area() == other.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __ge__(self, other):
        return self.area() >= other.area()
    def __le__(self, other):
        return self.area() <= other.area()
    
r1 = Rectangle(4,8)
r2 = Rectangle(14,18)
r3 = Rectangle(10,18)
r4 = Rectangle(3,7)

print(r1 > r2)
print(r3 == r2)
print(r4 < r1)
print(r3 >= r2)
print(r1 <= r3)