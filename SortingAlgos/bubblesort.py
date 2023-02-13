# bubble sort checks first item against second item, then second item to 3rd item, and then continue until end of list.
# A better way to think is compare n to n + 1 until end of list and flip the items if  n + 1 < n:
#
# Also to note, that the space complexity of the Bubble Sort is O(1) because you aren't creating a new list.

def bubble_sort(l1):
    for i in range(len(l1) - 1, 0, -1):
        for j in range(i):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1


temp = [1,2,3,4,5]
temp1 = [5,4,3,2,1]
temp2 = [5,1,3,4,2]

print(bubble_sort(temp))
print(bubble_sort(temp1))
print(bubble_sort(temp2))

