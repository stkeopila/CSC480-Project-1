import sys

# 4 (# of columns)
# 3 (# of rows)
# _ (empty cell)
# # (blocked cell)
# * (dirty cell)
# @ (robot starting location)

# example
# 4
# 3
# _*__
# __#*
# _@*#

if __name__ == '__main__':
    if sys.argv[1] == "uniform-cost":
        print("Uniform Cost")
    elif sys.argv[1] == "depth-first":
        print("Depth First")
    else:
        print("Error, Invalid input for search algorithm. Try 'uniform-cost' or 'depth-first'.")
        sys.exit()