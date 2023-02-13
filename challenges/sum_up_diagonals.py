def sum_up_diagonals(l1):
    # answer = 0
    # for y in range(len(l1)):
    #     answer += l1[y][y]
    # l1.reverse()
    # for y in range(len(l1)):
    #     answer += l1[y][y]
    # return answer

    # answer = 0
    # for y in range(len(l1)):
    #     answer += l1[y][y]
    #     answer += l1[y][-1-y]
    # return answer

    # return sum([l1[x][x] + l1[x][-1-x] for x in range(len(l1))])
    return sum([l1[x][x] + l1[x][-1-x] for x, val in enumerate(l1)])


list1 = [
    [1, 2],
    [3, 4]
]

print(sum_up_diagonals(list1))  # 10

list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum_up_diagonals(list2))  # 30

list3 = [
    [4, 1, 0],
    [-1, -1, 0],
    [0, 0, 9]
]

print(sum_up_diagonals(list3))  # 11

list4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(sum_up_diagonals(list4))  # 68