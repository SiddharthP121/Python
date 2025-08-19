'''
Question. Sum of all the integers in the file 
01. Any exception if encountered log it into the terminal
02. Execution of the code must not stopped after encountering the error
'''

with open('sum.txt', 'r') as sumFile:
    sum = 0
    for line in sumFile:
        try:
           print(line)
           value = int(line)
           sum += value
        except ValueError as ve:
            print('Value Error encountered ->', ve)
            continue
        except TypeError as te:
            print('Type Error encountered ->', te)
            continue
        except Exception as e:
            print('Exception encountered ->', e)
            continue
    print('The sum of all the intergers in the files is', sum)
