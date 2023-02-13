def find_the_duplicate(l1):
    for x in l1:
        if l1.count(x) > 1:
            return x



print(find_the_duplicate([1,2,1,4,3,12]))
print(find_the_duplicate([6,1,9,5,3,4,9]))
print(find_the_duplicate([2,1,3,4]))