class OutOfRangeException(Exception):
    def __init__(self, message):
        super().__init__(message)


def checkNum (num):
    
    if num > 100 or num < 0:
        raise OutOfRangeException('Invalid number entered')
    else:
        print('Number registered')


try:
    num = int(input('Enter any number\n'))
    checkNum(num)
except OutOfRangeException as OOR:
    print('Please enter the number between 1 to 100\n')
    print(OOR)
