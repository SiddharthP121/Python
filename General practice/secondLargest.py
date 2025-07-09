# second largest

my_list = [23, 45, 21, 54, 43]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            largest = my_list[i]
            secondLargest = my_list[j]
        else:
            largest = my_list[j]
            secondLargest = my_list[i]

print("The largest is", largest)
print("The Second largest is", secondLargest)