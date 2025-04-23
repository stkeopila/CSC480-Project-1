import sys
import heapq

def dfs(rob_loc):
    col, row, robot, dirty_cells, grid = rob_loc[0], rob_loc[1], rob_loc[2], rob_loc[3], rob_loc[4]
    path = []
    visited = set()
    cleaned = []
    nodes_generated = nodes_expanded = 0
    moves = [(-1, 0, "N"),(1, 0, "S"),(0, -1, "W"),(0, 1, "E")]
    def dfs_helper(new_pos):
        nonlocal nodes_expanded, nodes_generated
        nodes_expanded += 1
        if len(cleaned) == len(dirty_cells):
            return True
        for r, c, dir in moves:
            new_row, new_col = new_pos[0] + r, new_pos[1] + c
            next_pos = (new_row, new_col)
            nodes_generated += 1
            if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] != '#':
                new_spot = (next_pos, frozenset(cleaned))
                if new_spot not in visited:
                    visited.add(new_spot)
                    path.append(dir)
                    if grid[new_row][new_col] == '*' and next_pos not in cleaned:
                        cleaned.append(next_pos)
                        path.append('V')
                    if dfs_helper(next_pos):
                        return True
                    if path[-1] == 'V':
                        path.pop()
                        cleaned.pop()
                    path.pop()
        return False
    dfs_helper(robot)

    for dir in path:
        print(dir)
    print(F"{nodes_generated} nodes generated\n{nodes_expanded} nodes expanded")
    return path

def uniform_cost(rob_loc):
    found_all_dirty_cells = False
    nodes_expanded = nodes_generated = 0
    col, row, robot, dirty_cells, grid = rob_loc[0], rob_loc[1], rob_loc[2], rob_loc[3], rob_loc[4]
    heap = [(0, robot, 0, [], [])]
    visited = set([(robot, frozenset())])
    moves = [(-1, 0, "N"),(1, 0, "S"),(0, -1, "W"),(0, 1, "E")]
    while len(dirty_cells) != heap[0][2]: 
        for r, c, dir in moves:
            rob_row, rob_col = robot[0] + r, robot[1] + c
            if 0 <= rob_row < row and 0 <= rob_col < col and grid[rob_row][rob_col] != '#':
                nodes_generated += 1
                new_pos = (rob_row, rob_col)
                new_cleaned = list(heap[0][4])
                if grid[rob_row][rob_col] == '*' and new_pos not in heap[0][4]:
                    vaccum_path = heap[0][3] + [dir, "V"]
                    new_cleaned.append(new_pos)
                    new_spot = (new_pos, frozenset(new_cleaned))
                    if new_spot not in visited:
                        visited.add(new_spot)
                        heapq.heappush(heap, (heap[0][0] + 1, new_pos, heap[0][2] + 1, vaccum_path, new_cleaned))
                        if len(dirty_cells) == heap[0][2]:
                            found_all_dirty_cells = True
                else:
                    new_spot = (new_pos, frozenset(new_cleaned))
                    if new_spot not in visited:
                        heapq.heappush(heap, (heap[0][0] + 1, new_pos, heap[0][2], heap[0][3] + [dir], new_cleaned))
        if found_all_dirty_cells:
            break
        nodes_expanded += 1
        heapq.heappop(heap)
        robot = heap[0][1]
    for dir in heap[0][3]:
        print(dir)
    print(F"{nodes_generated} nodes generated\n{nodes_expanded} nodes expanded")

def find_info():
    dirty_cells = []
    grid = []
    starting_point = None
    with open(sys.argv[2], 'r') as f:
        columns = int(f.readline().strip())
        rows = int(f.readline().strip())
        for row in range(rows):
            line = f.readline().strip()
            grid.append(list(line))
            for col, cell in enumerate(line):
                if cell == '@':
                    starting_point = (row, col)
                elif cell == '*':
                    dirty_cells.append((row, col))
    for row in grid:
        print(row)
    return (columns, rows, starting_point, dirty_cells, grid)
    

if __name__ == '__main__':
    robot_loc = find_info()
    if sys.argv[1] == "uniform-cost":
        uniform_cost(robot_loc)
    elif sys.argv[1] == "depth-first":
        dfs(robot_loc)
    else:
        print("Error, Invalid input for search algorithm. Try 'uniform-cost' or 'depth-first'.")
        sys.exit()