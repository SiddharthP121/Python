'''
6.

        1
      1 2
    1 2 3
  1 2 3 4 
1 2 3 4 5 
'''
for i in range(6, 0, -1):
    for space in range(i-1):
        print(" ", end=" ")
    for j in range(1, 7-i):
        print(j, end=" ")
    print()

            