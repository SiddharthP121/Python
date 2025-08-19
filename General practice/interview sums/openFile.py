# file = None
# try:
#     file = open('data2.txt', '+a')
#     file.write('Python Programming')
#     file.seek(10)
#     file.write('Hello World')
#     file.seek(0)
#     data = file.read()
    
# except FileNotFoundError:
#     print('File not found')
# else:
#     print('Printing the data of the file\n')
#     print(data)
# finally:
#     print('Closing the resources')
#     if file is not None:
#         file.close()
    

try:
    with open('data3.txt', 'a+') as file2:
        file2.write('Python programming')
        file2.seek(10)
        file2.write('Hello world')
        file2.seek(0)
        print(file2.read())
except Exception:
    print('Something went wrong\n')
finally:
     print('End of program')

