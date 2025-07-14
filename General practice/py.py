# '''
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14



#     1
#   1 2 1
# 1 2 3 2 1


# '''

# for i in range(1, 5):
#     for space in range(4 - i):
#         print(" ", end= " ")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     for k in range(i -1, 0, -1):
#         print("*", end=" ")
    
#     print()





# # n = 1
# # for i in range(1, 6):
# #     for j in range(1, i+1):
# #         print(n, end=" ")
# #         n+=1
# #     print()

# # n = 1
# # for i in range(1, 6):
# #     print(f"{i} ")
# #     n+=1

# '''
#    1
#  1 * 1
# 1 * * 1
#  1 * 1
#    1
# '''

# # for i in range(1, 5):
# #     for spaces in range(5-i):
# #         print(" ", end=" ")
# #     for j in range(5, i, -1):
# #         print("*", end=" ")
# #     print()


'''
5 4 3 2 1 2 3 4 5
  4 3 2 1 2 3 4
    3 2 1 2 3 
      2 1 2
        1
      2 1 2
    3 2 1 2 3 
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5



'''

for i in range(69, 64, -1):
    for spaces in range(69-i):
        print(" ", end=" ")
    for j in range(i, 64, -1):
        print(chr(j), end=" ")
    for k in range(66, i+1 ):
        print(chr(k), end=" ")
    print()
for i in range(66, 70):
    for spaces in range(69-i):
        print(" ", end=" ")
    for j in range(i, 64, -1):
        print(chr(j), end=" ")
    for k in range(66, i+1 ):
        print(chr(k), end=" ")
    print()

