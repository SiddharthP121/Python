'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''
'''
def reverse(num):
    is_negative = False
    if num < 0:
        num = -num
        is_negative = True
    str_num = str(num)
    reversed_num_str = str_num[::-1]
    return '-'+ reversed_num_str if is_negative else reversed_num_str     

reversed_num = int(reverse(123))
print(reversed_num)
'''
def reverse_int(num):
    reversed_number = 0
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    while num > 0:
        digit = num % 10
        reversed_number = reversed_number * 10 + digit
        num  = num // 10
    return reversed_number - reversed_number * 2 if is_negative else reversed_number

print(reverse_int(1234))
