# return the index of the tupple with the largest sum

my_list = [(1, 2, 3), (2, 4, 5), (6, 7, 8)]

largestSum = 0


for tup in my_list:
    sum = 0
    for i in range(0, 3):
        sum = tup[i] + sum
    if sum > largestSum:
        largestSum = sum  
        index = i     
        

print(largestSum)
print(index)