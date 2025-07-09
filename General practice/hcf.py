num1 = int(input("Enter the first number \n"))
num2 = int(input("Enter the second number \n"))

andar = max(num1, num2)
bahr = min(num1, num2)

while andar % bahr > 0:
    remain = andar % bahr 
    andar = bahr
    bahr = remain

print(bahr)
