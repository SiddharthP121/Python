# remove duplicates from the list

my_list = [1, 2, 3, 4, 4, 5, 6]
my_list2 = []
for i in range(1, len(my_list)):
   if i not in my_list2:
      my_list2.append(i)

print(my_list2)
