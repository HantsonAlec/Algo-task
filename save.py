# def ids(board, final_board, limit):
#     visited = []
#     stack = [board]
#     count = 0
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             find_open_space(n)
#             visited.append(n)
#             print(n)
#             print(count)
#             for node in neighbors(n):
#                 stack.append(node)
#                 if node == final_board:
#                     stack.clear()
#                     print("Done")
#                     print(node)
#                     break


# WORKS with vISITED CHECK ON n
BOARD = [[1, 8, 2],
         [0, 4, 3],
         [7, 6, 5]]

FINAL_BOARD = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

limit = 9
open_space = (0, 2)
visited = []
children = []
parent = [0 for _ in range(181440)]
depth = 0
count = 0
# Find the open space in the puzzle


def find_open_space(n):
    global open_space
    for i in range(len(n)):
        for j in range(len(n[i])):
            if(n[i][j] == 0):
                open_space = (j, i)
                break


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
    stack = [board]
    for i in range(limit):
        if ids(stack, final_board, i):
            print("DONE")
            print(count)
            break


# PROBLEM=> How to check each node on level before going to nex level
def ids(stack, final_board, limit):
    global visited, depth, children, count
    limit += 1
    while stack:
        if depth <= limit:
            n = stack.pop()
            if n == final_board:
                stack.clear()
                print("Done")
                print(n)
                return True
            else:
                if n not in visited:
                    find_open_space(n)
                    visited.append(n)
                    print(n)
                    print(depth)
                    for node in neighbors(n):
                        children.append(node)
                if len(stack) == 0:
                    depth += 1
                    for stack_tem in children:
                        stack.append(stack_tem)
                    children.clear()
            count += 1
        else:
            count += 1
            print("Not found within depth limit")
            return False


IDS(BOARD, FINAL_BOARD, limit)
