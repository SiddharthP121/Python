add = lambda a, b: a + b
substract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: "Error" if b <= 0 else a / b

num1 = int(input("Enter first number \n"))
num2 = int(input("Enter second number \n"))
operator = input("Enter operator \n")

if operator == "+" :
   result = add( num1, num2 )
elif operator == "-" :
   result = substract( num1, num2 )
elif operator == "*" :
   result = multiply( num1, num2 )
elif operator == "/" :
   result = divide( num1, num2 )
else :
    print("Invalid operator entered\n")

print(f"{num1} {operator} {num2} = {result}")