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
