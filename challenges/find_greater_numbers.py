def find_greater_numbers(l1):
    cnt = 0
    for index, value1 in enumerate(l1[1::]):
        for value0 in l1[0:index+1]:
            if value1 > value0:
                cnt += 1
    return cnt


print(find_greater_numbers([1,2,3]))
print(find_greater_numbers([6,1,2,7]))
print(find_greater_numbers([5,4,3,2,1]))
print(find_greater_numbers([]))
