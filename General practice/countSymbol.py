

# s = "Hii my name is siddharth, I am 20. I am learning python from Anudeep Foundation. My hobies are playing chess, reading books, swimming and writing and creating code. Now it's your turn to tell me about ourself. Do you?"

# # s = input("Enter any sentence to know the details about it...")

# capital_alphabets = 0
# small_alphabets = 0
# num = 0
# spaces = 0
# special_symbol = 0



# for i in s:
#     if ord(i) == 32:
#         spaces = spaces + 1
#     elif 48<=ord(i) <= 58:
#         num+=1
#     elif 65 <= ord(i) <= 90:
#         capital_alphabets += 1
#     elif 97 <= ord(i) <= 122:
#         small_alphabets += 1
#     else:
#         special_symbol += 1

# print("Capital alphabets: ", capital_alphabets)
# print("Small alphabets: ", small_alphabets)
# print("Numbers: ", num)
# print("Spaces: ", spaces)
# print("Special Characters: ", special_symbol)


value = 42
formatedValue = "Value:%16d" % value
print(formatedValue)