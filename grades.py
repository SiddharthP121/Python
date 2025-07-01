
PERCENTAGES = float(input("Enter the percentage: \n"))

if PERCENTAGES>100 or PERCENTAGES<0 :
    print("Invalid value please provide the input between 1-100")
elif PERCENTAGES>85 :
    print("Grade A")    
elif PERCENTAGES>69.9 :
    print("Grade B")  
elif PERCENTAGES>54.9 :
    print("Grade C")  
else :
    print("Grade D")        