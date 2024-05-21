def num_of_escapes(width, height, adjacency_matrix, output_file_path):
    matrix_of_escapes = [[0] * width for _ in range(height)]

    for i in range(height):
        matrix_of_escapes[i][0] = 1

    char_value_per_column = [{} for _ in range(width)]

    for i in range(height):
        char = adjacency_matrix[i][0]
        char_value_per_column[0][char] = char_value_per_column[0].get(char, 0) + 1

    for j in range(1, width):
        for i in range(height):
            char = adjacency_matrix[i][j]
            if adjacency_matrix[i][j] != adjacency_matrix[i][j - 1]:
                matrix_of_escapes[i][j] += matrix_of_escapes[i][j - 1]
            matrix_of_escapes[i][j] += sum(item.get(char, 0) for item in char_value_per_column)

        for i in range(height):
            char = adjacency_matrix[i][j]
            char_value_per_column[j][char] = char_value_per_column[j].get(char, 0) + matrix_of_escapes[i][j]

    if height - 1 == 0:
        return write_output(output_file_path, matrix_of_escapes[0][width - 1])

    return write_output(output_file_path, matrix_of_escapes[0][width - 1] + matrix_of_escapes[height - 1][width - 1])


def read_file(file_path, output_file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        if not first_line:
            return None

        width, height = map(int, first_line.split(' '))
        adjacency_matrix = []
        for _ in range(height):
            next_line = list(file.readline().strip())
            adjacency_matrix.append(next_line)

    return num_of_escapes(width, height, adjacency_matrix, output_file_path)


def write_output(output_file_path, result):
    with open(output_file_path, 'w') as file:
        file.write(str(result))
