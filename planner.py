import sys

# python3 make_vacuum_world.py 5 7 0.15 3 > sample-5x7.txt

def uniform_cost(rob_loc):
    print(rob_loc)
    return None

def find_start():
    starting_point = None
    with open(sys.argv[2], 'r') as f:
        columns = f.read(1)
        rows = f.read(2)
        for row, line in enumerate(f):
            for col, cell in enumerate(line):
                if cell == '@':
                    starting_point = (col + 1, row)
                    break
    return starting_point
    

if __name__ == '__main__':
    robot_loc = find_start()
    if sys.argv[1] == "uniform-cost":
        print("Uniform Cost")
        uniform_cost(robot_loc)
    elif sys.argv[1] == "depth-first":
        print("Depth First")
    else:
        print("Error, Invalid input for search algorithm. Try 'uniform-cost' or 'depth-first'.")
        sys.exit()