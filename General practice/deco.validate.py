def verify(func):
    def wrapper(*args):
        print("Start")
        if all(x > 0 for x in args):
            return func(*args)
        else:
            print('Error encountered')
    return wrapper
@verify
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4))
print(add(1, -2, 3, 4))