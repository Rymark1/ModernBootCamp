# Insertion sort always starts with the second item in the list, and compares to the item before it.  This is basically
# the inverse of the bubble sort.  2 -> 1, 3 -> 2, 4 -> 3, etc.
# Each item walks back until we finally find the correct spot.
# Big O for this is O(n^2) at worst case if everything is sorted the wrong way.
# Best case is if most of the values are in place already, is going to be O(n)
#
# Also to note, that the space complexity of the Insertion Sort is O(1) because you aren't creating a new list.


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j >= 0:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


test = [1,2,4,3,5,6]
test1 = [2,1,4,3,5,6]
test2 = [4,6,9,2,4,3,2,1,4,3,5,6]
print(insertion_sort(test))
print(insertion_sort(test1))
print(insertion_sort(test2))
