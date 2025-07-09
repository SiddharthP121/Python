percentage = int(input("Enter the percentage: \n "))

if percentage > 100 or percentage < 0:
    print("please enter the valid value\n")
else :
    if percentage >= 85:
     choise = int(input("Please select the course of your choise\n 1. BCA \n 2. B.Com(H) \n"))
     if choise == 1:
        csMarks = int(input("Enter the marks for computer science\n"))
        if csMarks >=90:
            print("You are eligible of BCA")
        else:
            print("Minimum 90 marks required in computer science")
     elif choise == 2:
       mathMarks = int(input("Enter the marks of Maths"))
       if mathMarks>= 90:
            print("You are eligible for B.Com(H)\n")
       else:
          print("Minimum 90 Marks required in maths\n")
     else :
        print("Invalid value entered")
        
    
          
