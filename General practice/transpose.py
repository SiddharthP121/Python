'''
[
  [1,2,3]
  [4,5,6]
]

transpose
[
  [1,4],
  [2,5],
  [3,6]
]

'''

data = [
  [1,2,3],
  [4,5,6]
]

transpose = [[], [], []]
for i in range(3):
    for i in data:
        if len(i) == 0:
            transpose[0].append(i)
        elif len(i) == 1:
            transpose[1].append(i)
        else:
            transpose[2].append(i)


print(transpose)