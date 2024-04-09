def bfs(s, c, visited):
    strings, columns = len(grid), len(grid[0])
    queue = [(s, c)]
    visited.add((s, c))

    while queue:
        s, c = queue.pop(0)
        directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

        for i, j in directions:
            str2, col2 = s + i, c + j
            if (str2 in range(strings) and
                    col2 in range(columns) and
                    grid[str2][col2] == 1 and (str2, col2) not in visited):
                queue.append((str2, col2))
                visited.add((str2, col2))


def num_of_island(grid):
    strings, columns = len(grid), len(grid[0])
    islands = 0
    visited = set()

    for s in range(strings):
        for c in range(columns):
            if grid[s][c] == 1 and (s, c) not in visited:
                bfs(s, c, visited)
                islands += 1
    return islands


grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

print(f"Кількість островів: {num_of_island(grid)}")
