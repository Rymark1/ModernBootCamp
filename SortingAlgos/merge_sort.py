# assume we have a list [5,4,7,1,3,2,8,6].  Mergesort will break the list into individual lists.  Each item becomes
# its own list and they are single item lists.
# So we take [5,4,7,1,3,2,8,6] and break it into [5,4,7,1], [3,2,8,6], then [5,4],[7,1],[3,2],[8,6].
# Lastly, we break it into [5][4][7][1][3][2][8][6].
#
# Once the list is broken down into individual lists of 1 item a list, we then start sorting a merging the lits back
# together.  We make sorted lists in pairs of 2.  [4,5], [1,7], [2,3] [6,8].
# Then [1,4,5,7], [2,3,6,8], and finally [1,2,3,4,5,6,7,8]
# The final step ends up looping through both lists with 2 different indexes.  We check each and keep moving them into
# a new combined list.
#
# The big O for space complexity for this is O(n) for breaking down the list into items.  A list of 8 items becomes 8
# single item lists.
# The time complexity for breaking down the list is O(log n) because it splits in half until 1 remains, so 8 -> 4 -> 2.
# Putting the items back together require iterating through every item so that is O(n).  Combined, the big O is
# O(n log n).


def merge(l1, l2):
    combined = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            combined.append(l1[i])
            combined.append(l2[j])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1
        else:
            combined.append(l2[j])
            j += 1
    while i < len(l1):
        combined.append(l1[i])
        i += 1
    while j < len(l2):
        combined.append(l2[j])
        j += 1
    return combined


def merge_sort(l1):
    if len(l1) == 1:
        return l1
    mid_index = len(l1) // 2
    left = merge_sort(l1[:mid_index])
    right = merge_sort(l1[mid_index:])
    return merge(left, right)


temp1 = [1,3,7,8]
temp2 = [2,4,5,6]
temp3 = [1,3,6,7,8]
temp4 = [2,4,5,6]
temp5 = [9,3,7,4,10,2,3]

print(merge(temp1, temp2))
print(merge(temp3, temp4))

print(merge_sort(temp5))
