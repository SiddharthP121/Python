
# Question 6 	Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered by the user. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

angelOne = float(input("Enter the first angle of the triange\n"))
angleTwo = float(input("Enter the second angle of the triange\n"))
angleThree = float(input("Enter the third angle of the triange\n"))

if angelOne + angleTwo + angleThree == 180:
    print("This is the valid triangle")

else: 
    print("This is not a valid triangle")    