'''
       1
      1 1
     1 * 1
    1 * * 1
   1 * * * 1
  1 * * * * 1
 1 * * * * * 1
1 * * * * * * 1
 1 * * * * * 1
  1 * * * * 1
   1 * * * 1
    1 * * 1
     1 * 1
      1 1
       1
'''


for i in range(0, 8):
    for spaces in range(7 - i):
        print(" ", end="")
    for j in range(0, i+1 ):
        if j == 0 or j == i:
            print('1', end=" ")
        else:
            print("*", end=" ")
    print()

for i in range(6, -1, -1):
    for spaces in range(7 - i):
        print(" ", end="")
    for j in range(0, i+1 ):
        if j == 0 or j == i:
            print('1', end=" ")
        else:
            print("*", end=" ")
    print()


