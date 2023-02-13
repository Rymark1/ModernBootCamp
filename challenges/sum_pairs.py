def sum_pairs(l1, nbr):
    for x in range(len(l1)):
        for nbr2 in l1[x+1::]:
            if l1[x] + nbr2 == nbr:
                return [l1[x], nbr2]
    return []


print(sum_pairs([4,2,10,5,1], 6))
print(sum_pairs([11,20,4,2,1,5], 100))
print(sum_pairs([11,20,4,2,1,5], 9))
