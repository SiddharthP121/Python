# Contact us at support@anudip.org or tech.cmis@anudip.org
# create a list of mail ids using list comprehensions

# factorial of numbers using lc.
# [1,2,3,4,5]
# [1,2,6,24,120]

import math
string = "Contact us at support@anudip.org"
mail_list = [word for word in string.split(' ') if '@' in word]
print(mail_list)

list_ = [1,2,3,4,5]
fac_list = [math.factorial(n) for n in list_]
print(fac_list)
