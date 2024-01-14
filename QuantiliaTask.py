def count_life_around(grid, n, m, t):
    count = 0
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i != n or j != m):
                count += grid[i][j][t]
    return count
