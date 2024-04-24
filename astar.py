import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def get_neighbors(node, grid):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left
    for dx, dy in directions:
        new_x, new_y = node.x + dx, node.y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
            neighbors.append(Node(new_x, new_y, node))
    return neighbors

def reconstruct_path(node):
    path = []
    current = node
    while current is not None:
        path.append((current.x, current.y))
        current = current.parent
    return path[::-1]

def astar(grid, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(*start)
    goal_node = Node(*goal)
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            return reconstruct_path(current_node)

        closed_set.add((current_node.x, current_node.y))

        for neighbor in get_neighbors(current_node, grid):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor, goal_node)
            neighbor.f = neighbor.g + neighbor.h

            if any(node.f < neighbor.f and (node.x, node.y) == (neighbor.x, neighbor.y) for node in open_set):
                continue

            heapq.heappush(open_set, neighbor)

    return None

def print_grid_with_path(grid, path):
    border = '+' + '-' * (len(grid[0]) * 2 - 1) +'-' + '+'
    print(border)
    for i in range(len(grid)):
        row = '|'
        for j in range(len(grid[i])):
            if (i, j) in path:
                row += '  '
            else:
                row += f'{grid[i][j]} '
        row += '|'
        print(row)
    print(border)

# Example usage:

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1]
]

print("Enter start node coordinates --->")
sx = int(input('X : '))
sy = int(input('Y : '))
print("Enter Goal node coordinates --->")
gx = int(input('X : '))
gy = int(input('Y : '))
start = (sx, sy)
goal = (gx, gy)
path = astar(grid, start, goal)
if path:
    print_grid_with_path(grid, path)
    print("Path found:\n", path[:6],'\n',path[6:12],'\n',path[12:])
else:
    print("No path found")
