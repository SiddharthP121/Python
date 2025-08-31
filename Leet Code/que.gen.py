'''
Write a generator fibonacci(n) that yields the first n Fibonacci numbers
Write a generator prime_numbers(limit) that yields prime numbers up to limit.

'''
def fab_gen(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


for num in fab_gen(10):
    print(num, end=' ')

print('\n' * 2)


def prime_num(limit):
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

for prime in prime_num(20):
    print(prime)

print('\n' * 2)

def multiple(limit):
    for i in range(1, limit):
        yield i if i % 3 == 0 else False

limit = int(input("Enter the limit \n"))

for mul in multiple(limit):
    print(mul)




