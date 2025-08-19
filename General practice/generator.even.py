'''
numbers=[10,15,22,33,40,55,60]
even numbers and sum of all the even numbers

'''

def find_even(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            yield num
            count += num
    return count

numbers=[10,15,22,33,40,55,60]

res = find_even(numbers)
iter = iter(res)

while True:
    try:
        even = next(iter)
        print('Even no found', even)
    except StopIteration as e:
        print('The sum of even no is', e.value)
        break
    



