def three_odd_numbers(l1):
    for i, value in enumerate(l1):
        if i+4 > len(l1):
            return False
        if sum(l1[i:i+3]) % 2 != 0:
            return True
    return False


print(three_odd_numbers([1,2,3,4,5]))
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False
