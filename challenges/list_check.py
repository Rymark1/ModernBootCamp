def list_check(l1):
    return all(isinstance(x, list) for x in l1)


print(list_check([[],[1],[2,3], (1,2)]))
print(list_check([1, True, [],[1],[2,3]]))
print(list_check([[],[1],[2,3]]))
