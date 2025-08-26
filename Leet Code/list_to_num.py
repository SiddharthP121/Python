def list_to_num(l):
    place = 1
    num = 0
    for i in l:
        num = num + i * place
        place *= 10
    return num

l1 = [ 4, 7, 8, 6, 1 ]

print(list_to_num(l1))
