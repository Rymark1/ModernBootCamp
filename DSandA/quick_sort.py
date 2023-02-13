# Quicksort is a divide and conquer algorithm.  It uses the first item in the list as your pivot point.
# Take the following list - [4,6,1,7,3,2,5] we begin by looking at the second item.
# The second item 6 is greater than the pivot so nothing happens.
# Then we check the third item, 1, and swap it and the 6 because it's less than the first item we found which was
# greater than the pivot number.
# The current list is now [4,1,6,7,3,2,5]
# We then check the 7 and don't move it at all.
# Then the 3 gets moved in place and swaps with the 6 because it is the current first high value we found.
# The list is now [4,1,3,7,6,2,5]
# We then check the 2, and it is less than the pivot point, so it swaps with the 7.
# The list is now [4,1,3,2,6,7,5]
# The 5 is greater than the pivot point so nothing happens.
# The last action is then swapping the last low item we sorted for the pivot point.
# The list is now [2,1,3,4,6,7,5]
# We then run the same action on both halves that are left, so [2,1,3] and [6,7,5]
# The pivot is 2, and 1 is less than so nothing moves, and the 3 is greater so nothing moves, and then we swap the
# pivot point for the last low item found which is 1.
# The list is now [1,2,3,4,6,7,5]
# We then set the pivot point to 6 and check it against 7.  7 is greater so nothing happens, but then the 5 is less
# than the pivot point so we swap the 7 and 5.
# The list is now [1,2,3,4,6,5,7].
# We then swap the pivot point with the last low number found which is 5.
# The list is now [1,2,3,4,5,6,7]
#
# This sort method is O(n log n) for the best case and average case.  The worst case is if the data is already sorted.
# This is O(n^2).


def quick_sort_helper(l1, left, right):
    if left < right:
        pivot_index = pivot(l1, left, right)
        quick_sort_helper(l1, left, pivot_index-1)
        quick_sort_helper(l1, pivot_index + 1, right)
    return l1


def quick_sort(l1):
    return quick_sort_helper(l1, 0, len(l1)-1)


def pivot(l1, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if l1[i] < l1[pivot_index]:
            swap_index +=1
            l1[i], l1[swap_index] = l1[swap_index], l1[i]
    l1[pivot_index], l1[swap_index] = l1[swap_index], l1[pivot_index]
    return swap_index


list1 = [4,6,1,7,3,2,5]
print(quick_sort(list1))

print(list1)