
# Question 9	Write a program to calculate the monthly telephone bills as per the following rule: 
# Minimum Rs. 200 for upto 100 calls. 
# Plus Rs. 0.60 per call for next 50 calls. 
# Plus Rs. 0.50 per call for next 50 calls. 
# Plus Rs. 0.40 per call for any call beyond 200 calls. 


noOfCalls = int(input("Enter no of calls made this month:\n"))

if noOfCalls <=  100:
    monthlyBill = 200
elif noOfCalls <= 150 and noOfCalls > 100:
    extraCharge = (noOfCalls-100) * 0.60
    monthlyBill = 200 + extraCharge  # Calculate 0.60 per call after 100 calls ie. next 50 calls
elif noOfCalls <= 200 and noOfCalls > 150:
    chargeFor150Calls = ( noOfCalls - 100 ) * 0.60 + 200
    extraCharge = ( noOfCalls - 150 ) * 0.50
    monthlyBill = chargeFor150Calls + extraCharge
elif noOfCalls > 200:
    chargeFor200Calls = 200 + ( 50 * 0.6 ) + ( 50 * 0.40 ) # first 100 calls + next 50 calls + next 50 calls according to the rate
    monthlyBill = chargeFor200Calls + (noOfCalls - 200) * 0.40
else:
    print("Invalid Value Entered")

print("Your telephone bill for this month is :", monthlyBill)