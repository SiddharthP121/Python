file = None
try:
    file = open('data2.txt', 'r+')
    file.write('\nHey my name is siddharth')
    data = file.read()
    
except FileNotFoundError:
    print('File not found')
else:
    print('Printing the data of the file\n')
    print(data)
finally:
    print('Closing the resources')
    if file is not None:
        file.close()
    