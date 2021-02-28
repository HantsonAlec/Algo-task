BOARD = [[1, 8, 2],
         [0, 4, 3],
         [7, 6, 5]]

FINAL_BOARD = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

open_space = (0, 2)


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


def bs(board, final_board):
    visited_fb = []
    visited_bf = []

    actions_fb = [0 for _ in range(181440)]
    actions_bf = [0 for _ in range(181440)]

    queue_fb = [board]  # Add the initial cell into the queue
    queue_bf = [final_board]  # Add the initial cell into the queue
    memory_nodes = []

    while queue_fb and queue_bf:
        if queue_fb:
            n = queue_fb.pop(0)
            find_open_space(n)
            for node in neighbors(n):
                if node not in visited_fb:
                    print(node)
                    # Add to visited and count depth
                    visited_fb.append(node)
                    if(n not in visited_fb):
                        visited_fb.append(n)
                    actions_fb[visited_fb.index(
                        node)] = actions_fb[visited_fb.index(n)] + 1
                    queue_fb.append(node)
                    memory_nodes.append(node)
                    if node == final_board:
                        print("Done via fb")
                        print(node)
                        print(actions_fb[visited_fb.index(node)])
                        memory_nodes.clear()
                        queue_bf.clear()
                        queue_fb.clear()
                        break
        # Back to front
        if queue_bf:
            n = queue_bf.pop(0)
            find_open_space(n)
            for node in neighbors(n):
                if node not in visited_bf:
                    print(node)
                    # Add to visited and count depth
                    visited_bf.append(node)
                    if(n not in visited_bf):
                        visited_bf.append(n)
                    actions_bf[visited_bf.index(
                        node)] = actions_bf[visited_bf.index(n)] + 1
                    queue_bf.append(node)
                    # Check if middle has been found
                    if node in memory_nodes:
                        print("Done found middle")
                        print(node)
                        print(actions_bf[visited_bf.index(node)])
                        memory_nodes.clear()
                        queue_bf.clear()
                        queue_fb.clear()
                        break
                    memory_nodes.clear()
                    if node == board:
                        print("Done via bf")
                        print(node)
                        print(actions_bf[visited_bf.index(node)])
                        memory_nodes.clear()
                        queue_bf.clear()
                        queue_fb.clear()
                        break


bs(BOARD, FINAL_BOARD)
