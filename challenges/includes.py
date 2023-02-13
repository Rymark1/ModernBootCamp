def includes(c1, value, index=0):
    if isinstance(c1, dict):
        return value in c1.values()
    else:
        return value in c1[index::]


print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))
print(includes({ 'a': 1, 'b': 2 }, 1))
print(includes({ 'a': 1, 'b': 2 }, 'a'))
print(includes('abcd', 'b'))
print(includes('abcd', 'e'))