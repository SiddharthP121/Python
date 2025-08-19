'''
Create  decorator:
@log_time → logs execution time
Apply  to the  function and ensure it work correctly.
'''

import time

def log_time(func):
    def wrapper():
        start = time.time()
        print('The program is starting')
        func()
        end = time.time()
        diff = end - start
        print(f'The script executed in {diff} seconds !!!')
    return wrapper



@log_time
def greet():
    print('Hello, python')


greet()
