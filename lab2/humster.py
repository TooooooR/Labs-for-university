def find_max_hamsters(s, c, arr):
    humsters = 0
    for i in range(0, c):
        additional_list = sorted([x[0] + x[1] * i for x in arr])
        if sum(additional_list[:(i + 1)]) <= s:
            humsters = i + 1
        else:
            break
    return humsters


array = [[1, 3], [4, 0], [2, 2]]

print(find_max_hamsters(10, 3, array))
