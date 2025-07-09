#find the average of 5 number using while loop  

my_list = []

for i in range(5):
    count = i + 1
    num = int(input(f"Enter number {count}: \n"))
    my_list.append(num)

average = 0
sum = 0
i = 0

while i < len(my_list):
    sum += my_list[i]
    i += 1

average = sum / 5

print("Sum", sum)
print("Average", average)
