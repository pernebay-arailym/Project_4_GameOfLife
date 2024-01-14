def count_life_around(grid, n, m, t):
    count = 0
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i != n or j != m):
                count += grid[i][j][t]
    return count

def evolve_with_boundary(state, steps):
    pass

def evolve_without_boundary(state, steps):
    pass

#usage:
given_state = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

time = 5

result_with_boundary = evolve_with_boundary(given_state, time)
result_without_boundary = evolve_without_boundary(given_state, time)

print("Evolution with fixed boundary:")
for row in result_with_boundary:
    print(row)

print("\nEvolution without boundary:")
for row in result_without_boundary:
    print(row)
