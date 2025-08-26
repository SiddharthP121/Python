'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

sum_list = []

l1.reverse()
l2.reverse()

num1 = ''
num2 = ''

str_l1 = [str(n) for n in l1]
str_l2 = [str(n) for n in l2]
for n in str_l1:
    num1 += n

for n in str_l2:
    num2 += n

numb1 = int(num1)
numb2 = int(num2)

print(num1, num2)

sum = numb1 + numb2

print(sum)

sum_str = str(sum)

rev_sum_list = []
for i in sum_str:
    s = int(i)
    rev_sum_list.insert(0, s)

print(rev_sum_list)