class one:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a + self.b
class two(one):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def sum(self):
        return super().sum() + self.c


out  = two(1, 3, 4)
print(out.sum())
