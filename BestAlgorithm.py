# Best First Surch Algorithm

import copy
import operator
# START_BOARD = [[4, 3, 0],  # Alternative
#                [7, 1, 2],
#                [8, 6, 5]]
START_BOARD = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
FINAL_BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
childs = []
parent = [0 for _ in range(181440)]
path = []

# Check the path


def extract_path(visited):
    p = FINAL_BOARD
    path = []
    path.append(p)
    while p != START_BOARD:
        p = parent[visited.index(p)]
        path.append(p)
    path.reverse()
    return path


def displace(puzzle_box, FINAL_BOARD):  # find distance from acutal puzzel to final board
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if(puzzle_box[i][j] != FINAL_BOARD[i][j]):
                if(puzzle_box[i][j] != 0):
                    count = count+1
                else:
                    count = count
    return count


def move_left(puzzle_box, x, y):
    root = copy.deepcopy(puzzle_box)
    root[x][y], root[x][y-1] = root[x][y-1], root[x][y]
    return root


def move_right(puzzle_box, x, y):
    root = copy.deepcopy(puzzle_box)
    root[x][y], root[x][y+1] = root[x][y+1], root[x][y]
    return root


def move_up(puzzle_box, x, y):
    root = copy.deepcopy(puzzle_box)
    root[x][y], root[x-1][y] = root[x-1][y], root[x][y]
    return root


def move_down(puzzle_box, x, y):
    root = copy.deepcopy(puzzle_box)
    root[x][y], root[x+1][y] = root[x+1][y], root[x][y]
    return root


def findzero(puzzle_box):  # find 0-space
    for i in range(0, 3):
        for j in range(0, 3):
            if(puzzle_box[i][j] == 0):
                return i, j


def genrate_childs(puzzle_box, x, y):
    if y == 0 and x == 0:  # edges topleft
        child1 = move_right(puzzle_box, x, y)
        child2 = move_down(puzzle_box, x, y)
        childs = [child1, child2]
    elif y == 2 and x == 2:  # edge downright
        child1 = move_left(puzzle_box, x, y)
        child2 = move_up(puzzle_box, x, y)
        childs = [child1, child2]
    elif y == 0 and x == 2:  # edge downleft
        child1 = move_up(puzzle_box, x, y)
        child2 = move_right(puzzle_box, x, y)
        childs = [child1, child2]
    elif y == 2 and x == 0:  # edge topright
        child1 = move_down(puzzle_box, x, y)
        child2 = move_left(puzzle_box, x, y)
        childs = [child1, child2]

    # other position in the puzzle
    elif y == 2:
        child1 = move_down(puzzle_box, x, y)
        child2 = move_up(puzzle_box, x, y)
        child3 = move_left(puzzle_box, x, y)
        childs = [child1, child2, child3]
    elif x == 0:
        child1 = move_right(puzzle_box, x, y)
        child2 = move_down(puzzle_box, x, y)
        child3 = move_left(puzzle_box, x, y)
        childs = [child1, child2, child3]
    elif y == 0:
        child1 = move_right(puzzle_box, x, y)
        child2 = move_down(puzzle_box, x, y)
        child3 = move_up(puzzle_box, x, y)
        childs = [child1, child2, child3]
    elif x == 2:
        child1 = move_right(puzzle_box, x, y)
        child2 = move_up(puzzle_box, x, y)
        child3 = move_left(puzzle_box, x, y)
        childs = [child1, child2, child3]
    else:
        child1 = move_right(puzzle_box, x, y)
        child2 = move_down(puzzle_box, x, y)
        child3 = move_up(puzzle_box, x, y)
        child4 = move_left(puzzle_box, x, y)
        childs = [child1, child2, child3, child4]
    return childs


def set_x(Startboard2):
    x = []
    minimum = min(Startboard2, key=lambda x: x[0])
    min_val = minimum[0]
    for i in Startboard2:
        if i[0] == min_val:
            x.append(i)
    return x


def remove_from_Startboard(x, Startboard2):
    for i in x:
        Startboard2.remove(i)
    return Startboard2


def best_first_search(root):
    global path
    root_Puzzle = displace(root, FINAL_BOARD)+1  # Amount of displased cells
    Startboard2 = [[root_Puzzle, root]]  # discplaced cells and Start_board
    visited = []
    close = []
    step = 0
    keylist = []
    k = root_Puzzle
    v = 1
    while Startboard2:
        x = set_x(Startboard2)  # detect minimum

        remove_from_Startboard(x, Startboard2)
        for k in x:
            # if distance to finalboard is 0 extract path
            if displace(k[1], FINAL_BOARD) == 0:
                path = extract_path(visited)
                return step
            else:  # if not generate children
                s1, s2 = findzero(k[1])
                childs = genrate_childs(k[1], s1, s2)  # create children

                for i in childs:  # for all children find distance to starboard, append them to starboardlist
                    # calculate distance from children to finalboard
                    value = displace(i, FINAL_BOARD) + step
                    # add this combination to startbord2
                    Startboard2.append([value, i])
                    if i not in visited:
                        visited.append(i)
                        parent[visited.index(i)] = k[1]
                close.append(k[1])
        Startboard2.sort(key=lambda x: x[0])  # Sort Children in startboardlist
        step = step + 1  # add step
    return 0


print("START_BOARD:", START_BOARD)
print("START_BOARD:", FINAL_BOARD)
print('Searching...')
best_first_search(START_BOARD)
print("Best- First- Surch solution / Depth of solution:",
      len(path)-1)  # -1 because algo starts on depth 0
print("Path: ")
print(*path, sep='\n')
