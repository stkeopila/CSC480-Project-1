import sys

# python3 make_vacuum_world.py 5 7 0.15 3 > sample-5x7.txt

def uniform_cost():
    
    return None

if __name__ == '__main__':
    with open(sys.argv[2], 'r') as f:
        columns = print(f.read(1))
        rows = print(f.read(2))
    if sys.argv[1] == "uniform-cost":
        print("Uniform Cost")
    elif sys.argv[1] == "depth-first":
        print("Depth First")
    else:
        print("Error, Invalid input for search algorithm. Try 'uniform-cost' or 'depth-first'.")
        sys.exit()