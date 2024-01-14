def count_life_around(grid, n, m):
    live_neighbors = 0
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i != n or j != m):
                live_neighbors += grid[i][j]
    return live_neighbors

def is_alive(current_state, live_neighbors):
        if current_state == 0:
            return 1 if live_neighbors == 3 else 0
        else:
            return 0 if live_neighbors < 2 or live_neighbors > 3 else 1

def evolve_with_boundary(state, step):
    rows = len(state)
    cols = len(state[0])

    current_grid = state.copy()
    for _ in range(step):
        new_grid = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                live_neighbors = count_life_around(current_grid, i, j)
                new_grid[i][j] = is_alive(current_grid[i][j], live_neighbors)
        current_grid = new_grid

    return current_grid

def evolve_without_boundary(state, time):
    rows = len(state)
    cols = len(state[0])
    

    def count_life_around_without_boundary(grid, n, m):
        live_neighbors = 0
        for i in range(n-1, n+2):
            for j in range(m-1, m+2):
                live_neighbors += grid[i % rows][j % cols]
        return live_neighbors
    
    current_grid = state.copy()
    for _ in range(time):
        new_grid = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                live_neighbors = count_life_around_without_boundary(current_grid, i, j)
                new_grid[i][j] = is_alive(current_grid[i][j], live_neighbors)
        current_grid = new_grid

    return current_grid


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
