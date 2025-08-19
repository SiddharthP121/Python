'''
Create two decorators:

@log_time → logs execution time

@authenticate(user) → allows execution only if user is "admin"

Apply both to the same function and ensure both work correctly in any order.

input of role from user

'''
import time

def authenticate(role):
    def log_time(func):
            def wrapper():
                if role == 'admin':
                    start = time.time()
                    print('Script is start executing')
                    func()
                    end = time.time()
                    print(f'The script is executed in {end - start}seconds!!!')
                else:
                    print('Access Denied !!!')
                    return None
            return wrapper
    return log_time

role = input('Enter your role\n').lower()

@authenticate(role)
def greet():
    print('Hello', role)

greet()
    
