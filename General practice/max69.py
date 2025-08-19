num = 999696

num_str = str(num)

num_list = list(num_str)

print(num_list)
index = None
if '6' in num_list:
    index = num_list.index('6')
    num_list[index] = '9'


print(num_list)
num_str2 = ""
for i in num_list:
    num_str2 += i


print(int(num_str2))