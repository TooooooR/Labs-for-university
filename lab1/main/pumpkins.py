field = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]


def reverse_fonk(arr):
    return arr[::-1]


def find_robot_way(arr):
    robot_way = []
    m = len(arr)  # Кількість рядків в масиві
    n = len(arr[0])  # Кількість стовпців в масиві
    for i in range(m):
        if i % 2 == 0:
            robot_way.extend(arr[i])
        else:
            reversed_list = reverse_fonk(arr[i])
            robot_way.extend(reversed_list)
    return robot_way


print(find_robot_way(field))
