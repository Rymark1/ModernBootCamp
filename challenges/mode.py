def mode(l1):
    count = 0
    value = 0
    for x in set(sorted(l1)):
        if count < l1.count(x):
            value = x
            count = l1.count(x)
    return value


print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4
