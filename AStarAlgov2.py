#A* Algorithm
# StartNode = [[0, 4, 6],  # Alternative
#              [2, 3, 5],
#              [1, 7, 8]]
GoalNode = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal
StartNode = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]  # Start
distance = []  # list for distances
children = []  # list with children

bestchild = StartNode
open_space = (0, 2)
visited = []
parent = [0 for _ in range(181440)]
depth = 0
path = []
print("START_BOARD:", StartNode)
print("START_BOARD:", GoalNode)
print('Searching...')

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


def Findchildren(board, final_board):

    stack = [board]
    global visited, depth, children
    while stack:
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
            return False


while bestchild != GoalNode:
    children.clear()  # clear children qeue
    Findchildren(bestchild, GoalNode)  # find children
    depth += 1
    fsave = 100000  # high vaue of functaion f
    path.append(bestchild)
    print(children)
    for ch in children:  # for all children define heurisitic etc.
        if bestchild == GoalNode:  # if bestchild = goalnode than break it
            break
        else:
            StartNode = ch  # startnode is first child
            g = 0  # actions you need
            h = 0  # heuristic
            distance.clear()  # clear distance queue

            for i in range(len(StartNode)):
                for j in range(len(StartNode)):
                    if StartNode[i][j] != GoalNode[i][j]:
                        h += 1  # add 1 everytime a cell is misplaced - we count displaced cells not right-placed cells

            # Distance to the goal position of the cells
            for i in range(len(StartNode)):
                for j in range(len(StartNode)):  # for all cells
                    if (StartNode[i][j] == 0):   # if its 0 than pass
                        pass
                    else:  # find Distances: Compare position Goalnoade and position startnode, add distance to temp
                        if (GoalNode[0][0] == StartNode[i][j]):
                            distance.append(abs(i - 0) + abs(j - 0))

                        elif (GoalNode[0][1] == StartNode[i][j]):
                            distance.append(abs(i - 0) + abs(j - 1))

                        elif (GoalNode[0][2] == StartNode[i][j]):
                            distance.append(abs(i - 0) + abs(j - 2))

                        elif (GoalNode[1][0] == StartNode[i][j]):
                            distance.append(abs(i - 1) + abs(j - 0))

                        elif (GoalNode[1][1] == StartNode[i][j]):
                            distance.append(abs(i - 1) + abs(j - 1))

                        elif (GoalNode[1][2] == StartNode[i][j]):
                            distance.append(abs(i - 1) + abs(j - 2))

                        elif (GoalNode[2][0] == StartNode[i][j]):
                            distance.append(abs(i - 2) + abs(j - 0))

                        elif (GoalNode[2][1] == StartNode[i][j]):
                            distance.append(abs(i - 2) + abs(j - 1))

                        elif (GoalNode[2][2] == StartNode[i][j]):
                            distance.append(abs(i - 2) + abs(j - 2))

                        else:
                            # no other positions possible
                            print("this is not an 8-puzzle")

            for i in range(len(distance)):
                g += distance[i]  # sum of distances

            f = h + g  # function f = h + g

            # if child1(f) is smaller than child2(f) than save this child as "best child"
            if f < fsave:
                fsave = f
                bestchild = StartNode

print(f"A* / Depth of solution: {depth}")
path.append(GoalNode)
print("Path: ")
print(*path, sep='\n')
