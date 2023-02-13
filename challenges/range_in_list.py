def range_in_list(l1, start=0, end=0):
    if end == 0:
        end = len(l1)
    return sum(l1[start:end+1])


print(range_in_list([1,2,3,4],0,2))
print(range_in_list([1,2,3,4],0,3))
print(range_in_list([1,2,3,4],1))
print(range_in_list([1,2,3,4]))
print(range_in_list([1,2,3,4],0,100))
print(range_in_list([],0,1))