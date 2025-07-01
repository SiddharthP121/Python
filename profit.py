
# Question 4 	Write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred. Cost price and selling price of an item is input by the user.

costPrice = float(input("Enter the cost price for the item\n"))
sellingPrice = float(input("Enter the selling price for the item\n"))

if costPrice > sellingPrice: 
    loss = costPrice - sellingPrice
    print("Loss of rs ",loss)

else:
    profit = sellingPrice - costPrice
    print("Profit of rs ",profit)