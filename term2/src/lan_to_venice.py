def lan_to_venice(matrix):
    length = len(matrix)
    vertices = [False] * length
    vertices[0] = True
    num_of_edges = 0
    length_of_cable = 0

    while num_of_edges < length - 1:
        minimum = float('inf')
        x = 0
        for i in range(length):
            if vertices[i]:
                for j in range(length):
                    if vertices[j] is False and matrix[i][j] != 0 and matrix[i][j] < minimum:
                        minimum = matrix[i][j]
                        x = j

        vertices[x] = True
        num_of_edges += 1
        length_of_cable += minimum

    return length_of_cable


def read_file(file):
    file = open(file, 'r')
    first_linex = file.readline()
    if not first_linex:
        file.close()
        return None

    first_line = list(map(int, first_linex.split(";")))
    adjacency_matrix = [first_line]
    for _ in range(len(first_line) - 1):
        adjacency_matrix.append(list(map(int, file.readline().split(';'))))
    file.close()

    return lan_to_venice(adjacency_matrix)
