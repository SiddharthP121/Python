# Question 8 	In a company an employee is paid as under: 
# If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary 
# and DA = 90% of basic salary.
# If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 
# and DA = 98% of basic salary. 
# If the employee's salary is input by the user write a program to find his gross salary. 


employeeSalary = int(input("Enter your basic monthly salary:\n"))

if employeeSalary < 1500 :
    hra = employeeSalary * 10 / 100
    da =  employeeSalary * 90 / 100

elif employeeSalary >= 1500 : 
    hra = 500
    da = employeeSalary * 98 / 100

grossSalary = employeeSalary + hra + da 

print("Your overall gross salary is:\n" ,grossSalary)
