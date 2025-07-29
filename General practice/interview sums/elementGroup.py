'''
Group values by keys (from list of tuples) input : [('fruit', 'apple'), ('fruit', 'banana'), ('color', 'red')] output : {'fruit': ['apple', 'banana'], 'color': ['red']}
'''

my_list = [('fruit', 'apple'), ('fruit', 'banana'), ('color', 'red'), ('cloth', 'shirt'), ('electronics', 'mobile'), ('cloth', 'top'), ('electronics', 'laptop')]

my_dict = {}

for tup in my_list:
    if tup[0] in my_dict:
        my_dict[tup[0]].append(tup[1])
    else:
        my_dict[tup[0]] = []
        my_dict[tup[0]].append(tup[1])

print(my_dict)
