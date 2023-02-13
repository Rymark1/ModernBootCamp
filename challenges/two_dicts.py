def two_list_dictionary(l1, l2):
    return {a: l2[l1.index(a)] if l1.index(a) < len(l2) else None for a in l1}


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
print(two_list_dictionary(['x', 'y', 'z'], [1, 2]))


# a = ["John", "Charles", "Mike"]
# b = ["Jenny", "Christy", "Monica", "Vicky"]
# x = dict(zip(a,b))
# print(x)
#
# a = ["John", "Charles", "Mike", "tony", "Billy"]
# b = ["Jenny", "Christy", "Monica", "Vicky"]
# x = dict(zip(a,b))
# print(x)
#
# a = ["John", "Charles", "Mike"]
# b = ["Jenny", "Christy", "Monica"]
# x = dict(zip(a,b))
# print(x)
