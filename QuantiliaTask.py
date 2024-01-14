def count_life_around(grid, n, m, t):
    live_neighbors = 0
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i != n or j != m):
                live_neighbors += grid[i][j][t]
    return live_neighbors

def is_alive(current_state, live_neighbors):
        if current_state == 0:
            return 1 if live_neighbors == 3 else 0
        else:
            return 0 if live_neighbors < 2 or live_neighbors > 3 else 1

def evolve_with_boundary(state, steps):
    rows = len(state)
    cols = len(state [0])
    pass

def evolve_without_boundary(state, steps):
    rows = len(state)
    cols = len(state[0])
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
