def floyd_warshall(adjacency_matrix):
    length = len(adjacency_matrix)
    matrix = adjacency_matrix
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix


def count_sum(matrix):
    length = len(matrix)
    lenght_of_cabel = 0
    floyd_warshall_mtr = floyd_warshall(matrix)
    for i in range(length):
        for j in range(length):
            lenght_of_cabel += floyd_warshall_mtr[i][j]

    return lenght_of_cabel // 2


def read_file(file):
    inf = 99999
    with open(file, 'r') as file:
        first_linex = file.readline()
        if not first_linex:
            return None

        first_line = first_linex.strip().split(";")
        first_line = [int(item) if item != "INF" else inf for item in first_line]
        adjacency_matrix = [first_line]
        for _ in range(len(first_line) - 1):
            row = file.readline().strip().split(';')
            row = [int(item) if item != "INF" else inf for item in row]
            adjacency_matrix.append(row)

    return floyd_warshall(adjacency_matrix)
