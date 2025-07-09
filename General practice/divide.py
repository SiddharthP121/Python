
def divide(a, b):
    return a/b

divider = int(input("Enter the divider\n"))
divident = int(input("Enter the divident\n"))
if divider < 1:
    print("Enter the valid value to divide\n")
else:
    result = divide(divider, divident)
    print(result)