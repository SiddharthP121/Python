
# Question 3 	Write a program to calculate the total expenses. Quantity and price per item are input by the user and discount of 10% is offered if the expense is more than 5000.

price = float(input("Enter the price for the item\n"))
noOfItem = int(input("Enter the number of item bought\n"))

total = price * noOfItem

if total > 5000 :
   discountedPrice = total * 5 /100
   total = total - discountedPrice

print("Total bill\n", total)