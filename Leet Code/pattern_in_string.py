"""
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I     N
A   L S   I G
Y A   H R
P     I

P0      I6        N12
A1   L5 S7    I11 G13
Y2 A4   H8 R10
P3      I9

s = "P AYPAL I SHIRI N G" iteration 1
AYPALSHIRIG

"""

s = "PAYPALISHIRING" # "AYPALSHIRIG"

rows=4

for row in range(rows, 0, -1):
    for j in range(0, row):
        print('*', end=' ') if j == 0 or j == row-1 else print(' ', end=' ')
    print('  ' * (rows - row), end='' )
    for j in range(0, row):
        print('*', end=' ') if j == 0 or j == row-1 else print(' ', end=' ')
        
    print()
    


