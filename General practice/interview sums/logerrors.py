'''
Write a program that takes a list of numbers and divides 100 by each.
Catch any ZeroDivisionError or TypeError and log the error with line number
to a file named "error_log.txt".

Example Input: [10, 0, 'a', 25]
Output:
100 / 10 = 10.0
Logged ZeroDivisionError
Logged TypeError
100 / 25 = 4.0
'''

n = 5
divList = []
for i in range(n):
    num = input(f'Enter number {i+1}\n')
    divList.append(num)

with open('divRes.txt', 'a+') as divRes:
        for index, i in enumerate(divList, start=1):
            try:
                divisor = int(i)
                print(f'{index} = 100 / {i} = {100 / divisor}\n')
            except TypeError as te:
                 divRes.write(f'Line {index} = Logged Type Error = {te} \n')
                 print(f'Line {index} = Logged Type Error = {te} \n')
            except ValueError as ve:
                 divRes.write(f'Line {index} = Logged Value Error = {ve} \n')
                 print(f'Line {index} = Logged Value Error = {ve} \n')
            except ZeroDivisionError as ze:
                 divRes.write(f'Line {index} = Logged Zero division Error = {ze}\n')
                 print(f'Line {index} = Logged Zero division Error = {ze}\n')
            except Exception as e:
                 divRes.write(f'Line {index} = Exception here\n')
        divRes.seek(0)
        print(divRes.read())
        
            
                 

    
        



