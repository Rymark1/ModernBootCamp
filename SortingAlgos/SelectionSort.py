# For selection sort, you need to have the indexs of each value.  When we track the first item, we check and store the
# current min index.  Then we start a for loop the next item over and check if it is less than the current min index.
# If it is, we update the value until we iterate through the whole list.  Once you find the min index, you swap the
# first item in the list with the min index list, then go to the next item and iterate through the list repeating.
#
# Also to note, that the space complexity of the Selection Sort is O(1) because you aren't creating a new list.

def selection_sort(l1):
    for idx in range(len(l1) - 1):
        min_idx = idx
        for i, _ in enumerate(l1[idx::]):
            if l1[min_idx] > l1[i + idx]:
                min_idx = i + idx
        l1[idx], l1[min_idx] = l1[min_idx], l1[idx]
    return l1


def selection_sort1(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list



temp = [1,2,3,4,5]
temp1 = [5,4,3,2,1]
temp2 = [5,1,3,4,2]

print(selection_sort(temp))
print(selection_sort(temp1))
print(selection_sort(temp2))
