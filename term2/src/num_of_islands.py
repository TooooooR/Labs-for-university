def bfs(x, y, visited):
    strings, columns = len(grid), len(grid[0])
    queue = [(x, y)]
    visited.add((x, y))

    while queue:
        x, y = queue.pop(0)
        directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

        for i, j in directions:
            x2, y2 = x + i, y + j
            if (x2 in range(strings) and
                    y2 in range(columns) and
                    grid[x2][y2] == 1 and (x2, y2) not in visited):
                queue.append((x2, y2))
                visited.add((x2, y2))


def num_of_island(grid):
    strings, columns = len(grid), len(grid[0])
    islands = 0
    visited = set()

    for x in range(strings):
        for y in range(columns):
            if grid[x][y] == 1 and (x, y) not in visited:
                bfs(x, y, visited)
                islands += 1
    return islands


grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

print(f"Кількість островів: {num_of_island(grid)}")
