def nth(l1, n1):
    return l1[n1] if n1 >= 0 else l1[len(l1) + n1]



print(nth(['a', 'b', 'c', 'd'], 1))  # 'b'
print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'
