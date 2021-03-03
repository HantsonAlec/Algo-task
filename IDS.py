# IDS Algorithm
#Start and finish
BOARD = [[1, 8, 2],
         [0, 4, 3],
         [7, 6, 5]]
# BOARD = [[4, 3, 0], #Alternative
#          [7, 1, 2],
#          [8, 6, 5]]
FINAL_BOARD = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

limit = 20
open_space = (0, 2)
visited = []
children = []
parent = [0 for _ in range(181440)]
depth = 0

print("START_BOARD:", BOARD)
print("START_BOARD:", FINAL_BOARD)
print('Searching...')


# Check the path
def extract_path():
    p = FINAL_BOARD
    path = []
    path.append(p)
    while p != BOARD:
        p = parent[visited.index(p)]
        path.append(p)
    path.reverse()
    return path


# Find the open space in the puzzle
def find_open_space(n):
    global open_space
    for i in range(len(n)):
        for j in range(len(n[i])):
            if(n[i][j] == 0):
                open_space = (j, i)
                break


# Look for possible next steps
def neighbors(n):
    res = []
    x = open_space[0]
    y = open_space[1]
    options = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for option in options:
        board_copy = list(map(list, n))
        if (option[0] in [0, 1, 2] and option[1] in [0, 1, 2]):
            replaced_number = board_copy[option[1]][option[0]]
            board_copy[option[1]][option[0]] = 0
            board_copy[y][x] = replaced_number
            res.append(board_copy)
    return res


def IDS(board, final_board, limit):
    found = False
    stack = [board]
    # Iterate through depth limits
    for i in range(0, limit):
        if ids(stack, final_board, i):
            print(f"IDS / Depth of solution: {depth}")
            print("Path: ")
            print(*extract_path(), sep='\n')
            found = True
            break
    if not found:
        print(f"Not found within depth limit {limit}")


def ids(stack, final_board, limit):
    global visited, depth, children
    limit += 1
    while stack:
        # Check if limit reached
        if depth <= limit:
            n = stack.pop()
            if n == final_board:
                stack.clear()
                return True
            else:
                find_open_space(n)
                visited.append(n)
                for node in neighbors(n):
                    if node not in visited:
                        visited.append(node)
                        children.append(node)
                        parent[visited.index(node)] = n
                if len(stack) == 0:
                    depth += 1
                    for stack_tem in children:
                        stack.append(stack_tem)
                    children.clear()
        else:
            return False


IDS(BOARD, FINAL_BOARD, limit)
