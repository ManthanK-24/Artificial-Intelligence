def bfs_pacman(grid, start, end):
    queue = [start]
    explored = set()

    while queue:
        current_node = queue.pop(0)
        row, col = current_node

        if current_node == end:
            break

        if current_node not in explored:
            explored.add(current_node)
            print(row, col)

            # Enqueue neighbors in the specified order (UP, LEFT, RIGHT, DOWN)
            for neighbor in [(row-1, col), (row, col-1), (row, col+1), (row+1, col)]:
                n_row, n_col = neighbor
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and grid[n_row][n_col] != '%':
                    queue.append((n_row, n_col))

    return explored


# Read input
pacman_pos = tuple(map(int, input().split()))
food_pos = tuple(map(int, input().split()))
rows, cols = map(int, input().split())

grid = [input().strip() for _ in range(rows)]

# Perform BFS
explored_nodes = bfs_pacman(grid, pacman_pos, food_pos)

# Print the result
print(len(explored_nodes))
for node in explored_nodes:
    print(node[0], node[1])

# Calculate and print distance
distance = len(explored_nodes) - 1
# print("D")
for i in range(distance + 1):
    print(explored_nodes[i][0], explored_nodes[i][1])
