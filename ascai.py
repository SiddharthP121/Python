# Question 11	Any character is entered by the user; write a program to determine whether the character entered is a capital letter, a small case letter, a digit or a special symbol. The following table shows the range of ASCII values for various characters. 
# Characters 	ASCII Values 
# A – Z 	65 – 90
# a – z 	97 – 122

character = str(input("Enter the character you want to Identify\n"))

if ord(character) >= 65 and ord(character) <= 90 :
    print("The entered character is capital letter and its ASCAII value is :", ord(character))
elif ord(character) >= 97 and ord(character) <= 122 :
    print("The entered character is small letter and it's ASCII value is :", ord(character))
else: 
    print("Invalid value entered please enter any alphabet character")