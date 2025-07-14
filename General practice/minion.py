def minion_game(string):
    # your code goes here
    s = string.upper()
    kevin_points = 0
    stuart_points = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            p1 = s[i]
            p2 = s[i+1:j+1]
            if p1 == 'A' or p1 == 'E' or p1 == 'I' or p1 == 'O' or p1 == 'U':
                print(p1,p2)
                kevin_points += 1
            else: 
                stuart_points += 1
                print(p1,p2)
    
    print(kevin_points)
    print(stuart_points)

s = 'BAANANAS'
minion_game(s)