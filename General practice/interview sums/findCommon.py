# find common elements in 2 lists

my_list1 = [1, 2, 3, 4, 5]
my_list2 = [4, 5, 6, 7, 8]
same_items = []

for i in my_list1:
    if i in my_list2:
        same_items.append(i)

print(same_items)

