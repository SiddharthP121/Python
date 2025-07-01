# Question 5 	If the ages of Ram, Sulabh and Ajay are input by the user, write a program to determine the youngest of the three.

ageRam = int(input("Enter the age of Ram\n"))
ageSulabh = int(input("Enter the age of Sulabh\n"))
ageAjay = int(input("Enter the age of Ajay\n"))

if ageRam < ageSulabh and ageRam < ageAjay:
    print("Ram is the youngest")

elif ageSulabh < ageRam and ageSulabh < ageAjay:
    print("Sulabh is the youngest")

else :
    print("Ajay is the youngest")    