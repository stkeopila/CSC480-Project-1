import sys
import heapq

# python3 make_vacuum_world.py 5 7 0.15 3 > sample-5x7.txt
# heap = [Cost, robot_location, how many dirty cells cleaned, Vacuum Path, cleaned locations]

# def dfs(rob_loc):
#     return None
#     found_all_dirty_cells = False
#     nodes_expanded = nodesgenerated = 0
#     col, row, robot, dirty_cells, grid = rob_loc[0], rob_loc[1], rob_loc[2], rob_loc[3], rob_loc[4]
#     heap = [(0, robot, 0, [], [])]
#     visited = set([(robot, frozenset())])
#     moves = [(-1, 0, "N"),(1, 0, "S"),(0, -1, "W"),(0, 1, "E")]
#     while len(dirty_cells) != heap[0][2]:
#         for r, c, dir in moves:
#             rob_row, rob,col = robot[0] + r, robot[1] + c
#             if 0 <= rob_row < row and 0 <= rob_col < col and grid[rob_row][rob_col] != '#':
#                 nodes_generated += 1
#                 nodes_expanded += 1
#                 new_pos = (rob_row, rob_col)
#                 new_cleaned = list(heap[0][4])
#                 if grid[rob_row][rob_col] == '*' and new_pos not in heap[0][4]:

# need to store previous robot location so i dont research the area
# return back a int value when found a dirty cell
# 

# heap = [Cost, robot_location, how many dirty cells cleaned, Vacuum Path, cleaned locations]
# stack = [robot location, path, visited states, how many dirty cells cleaned]

# return (columns, rows, starting_point, dirty_cells, grid)
# dfs(robot_loc, visited, path, moves)

def dfs(rob_loc, visited, path, moves): 
    visited.add(rob_loc[2])
    grid = rob_loc[4]
    for r, c, dir in moves:
        rob_row, rob_col = rob_loc[2][0] + r, rob_loc[2][1] + c
        new_pos = (rob_row, rob_col)
        if new_pos not in visited:
            path.append(dir)
            rob_loc[2] = new_pos
            if grid[rob_row][rob_col] == '*':
                path.append('V')
            dfs(rob_loc, visited, path, moves)

# vististed.remove()
        

    
    


# def dfs(rob_loc):
#     found_all_dirty_cells = False
#     nodes_expanded = nodesgenerated = 0
#     col, row, robot, dirty_cells, grid = rob_loc[0], rob_loc[1], rob_loc[2], rob_loc[3], rob_loc[4]
#     moves = [(-1, 0, "N"),(1, 0, "S"),(0, -1, "W"),(0, 1, "E")]
#     dfs_helper(rob_loc)



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
    # print(f"Cost: {heap[0][0]} Found:", heap[0][3])
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
        visited = set()
        path = []
        moves = [(-1, 0, "N"),(1, 0, "S"),(0, -1, "W"),(0, 1, "E")]
        dfs(robot_loc, visited, path, moves)
    else:
        print("Error, Invalid input for search algorithm. Try 'uniform-cost' or 'depth-first'.")
        sys.exit()