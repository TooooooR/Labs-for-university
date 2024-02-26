field = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]


def find_robot_way(arr):
    additional_list = []
    robot_way = []
    strings = len(arr)
    columns = len(arr[0])
    for i in range(columns):
        for j in range(strings):
            additional_list.append(arr[-(j + 1)][-(i + 1)])
        if i % 2 != 0:
            additional_list.reverse()
        robot_way.extend(additional_list)
        additional_list = []

    return robot_way


print(find_robot_way(field))
