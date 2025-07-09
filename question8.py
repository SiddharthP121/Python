'''
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1

'''

for i in range(1, 6):
    for space in range(0, i):
        print(" ", end="")
    for j in range(1, 7-i):
        print(j, end=" ")
    print()