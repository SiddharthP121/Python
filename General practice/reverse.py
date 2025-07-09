num = int(input("Enter any number \n"))
orignal = num
if num <= 0:
    print("Enter any number greater than zero")
else:
    reversed_num = 0
    while num > 0:
       
        digit = num % 10   
        reversed_num = reversed_num * 10 + digit 
        num = num // 10           

print(f"Reversed number of {orignal} is {reversed_num}")
