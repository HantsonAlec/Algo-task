BOARD = [[2, 8, 1],
         [4, 7, 3],
         [0, 6, 5]]

FINAL_BOARD = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

limit = 3
open_space = (0, 2)


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
    for i in range(limit):
        if ids(board, final_board, i):
            print("DONE")
            break


def ids(board, final_board, limit):
    visited = []
    stack = [board]
    count = 0
    while stack:
        n = stack.pop()
        find_open_space(n)
        if count <= limit:
            for node in neighbors(n):
                print(node)
                if node not in visited:
                    visited.append(node)
                    stack.append(node)
                    if node == final_board:
                        stack.clear()
                        return True
                    # else:
                    #     ids(node, final_board, limit)
                    #     break
            count += 1
        else:
            break


IDS(BOARD, FINAL_BOARD, limit)
