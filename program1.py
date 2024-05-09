def explore_island(grid, row, col, visited):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited[row][col] = True

    for d in directions:
        new_row, new_col = row + d[0], col + d[1]
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "L" and not visited[new_row][new_col]:
            explore_island(grid, new_row, new_col, visited)

def count_islands(grid):
    if not grid:
        return 0
    
    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False] * num_cols for _ in range(num_rows)]
    island_count = 0
    
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "L" and not visited[i][j]:
                # If the cell is land and not visited, explore the island
                explore_island(grid, i, j, visited)
                # Increment the island count after exploring the entire island
                island_count += 1
                
    return island_count
