import heapq

def manhattan_heuristic(node, destination):
    return abs(node[0] - destination[0]) + abs(node[1] - destination[1])

def astar_pacman(grid, start, end):
    heap = [(0, start)]
    explored = set()

    while heap:
        cost, current_node = heapq.heappop(heap)
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
                    neighbor_cost = cost + 1 + manhattan_heuristic(neighbor, end)
                    heapq.heappush(heap, (neighbor_cost, neighbor))

    return explored


# Read input
pacman_pos = tuple(map(int, input().split()))
food_pos = tuple(map(int, input().split()))
rows, cols = map(int, input().split())

grid = [input().strip() for _ in range(rows)]

# Perform AStar search
explored_nodes = astar_pacman(grid, pacman_pos, food_pos)

# Print the result
print(len(explored_nodes))
for node in explored_nodes:
    print(node[0], node[1])

# Calculate and print distance
distance = manhattan_heuristic(pacman_pos, food_pos)
print(distance + 1)
for i in range(distance + 1):
    print(explored_nodes[i][0], explored_nodes[i][1])
