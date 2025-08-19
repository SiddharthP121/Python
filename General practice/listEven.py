'''
data = [[10, 15, 20], [25, 30], [35, 40, 45]]
filter all the even numbers and create a new list.

'''

data = [[10, 15, 20], [25, 30], [35, 40, 45]]


even_list = [even for lists in data for even in lists if even % 2 == 0]
print(even_list)

even_sub_list = [[even_num for even_num in even_num_list if even_num % 2 == 0] for even_num_list in data]
print(even_sub_list)