# .Count frequency of elements in a list.

# my_list1 = [1, 2, 3, 4, 5, 2, 3, 1, 3, 4, 5, 1, 4]
my_list1 = ['mango', 'orange', 'apple', 'pineapple', 'banana', 'orange', 'pineapple', 'mango', 'banana', 'apple', 'pineapple', 'orange', 'mango', 'banana']

my_set = set(my_list1)
print(my_set)

for i in my_set:
    count  = 0
    for j in range(0, len(my_list1)):
        if i == my_list1[j]:
            count+=1
    print(f'{i} = {count}')
         

