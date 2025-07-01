
# Question 10	The marks obtained by a student in 5 different subjects are input by the user. The student gets a division as per the following rules:
# Percentage above or equal to 60 - First division 
# Percentage between 50 and 59 - Second division 
# Percentage between 40 and 49 - Third division 
# Percentage less than 40 - Fail 
# Write a program to calculate the division obtained by the student. 

mathMarks = int(input("Enter the marks obtained in Maths: \n"))
englishMarks = int(input("Enter the marks obtained in English: \n"))
scienceMarks = int(input("Enter the marks obtained in Science: \n"))
hindiMarks = int(input("Enter the marks obtained in Hindi: \n"))
computerMarks = int(input("Enter the marks obtained in Computer: \n"))

if mathMarks < 0 or mathMarks > 100:
    print("Invalid Math marks!")
elif englishMarks < 0 or englishMarks > 100:
    print("Invalid English Marks")
elif scienceMarks < 0 or scienceMarks > 100:
    print("Invalid English Marks")
elif hindiMarks < 0 or hindiMarks > 100:
    print("Invalid English Marks")
elif englishMarks < 0 or englishMarks > 100:
    print("Invalid English Marks")



percentage = ( mathMarks + englishMarks + scienceMarks + hindiMarks + computerMarks ) / 5

print("Your percentage is: ", percentage)

if percentage >= 60: 
    print("\nCongratulations!!! You are passed with FIRST DIVISION!")
elif percentage > 50 and percentage <= 59:
    print("\nGood!! Your are passed with SECOND DIVISION!") 
elif percentage > 40 and percentage <= 49:
    print("\n Your are passed with THIRD DIVISION!") 
else :
    print("\n Your are FAILED!") 
