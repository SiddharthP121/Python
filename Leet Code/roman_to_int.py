'''

romn_dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000 
}
s =  "IV"
num = 0
prev_num = 0
for i in reversed(s):
    value = romn_dict[i]
    if value < prev_num:
        num -= value
    else:
        num += value
        prev_num = value
    

print(num)
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        num = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                num -= roman[a]
            else:
                num += roman[a]
        
        return num + roman[s[-1]]