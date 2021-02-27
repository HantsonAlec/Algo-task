board = [[4, 2, 7],
         [1, 6, 3],
         [0, 8, 5]]

FINAL_BOARD = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]

# START_FB = (0, 2)
# START_BF = (2, 2)

open_space = (0, 2)


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


def bs(states):
    # NOT_VISITED, VISITED = 0, 1
    visited_fb = []
    visited_bf = []
    visited_fb = []
    actions_fb = [0 for _ in range(181440)]
    actions_bf = [0 for _ in range(181440)]
    queue_fb = [board]  # Add the initial cell into the queue
    queue_bf = [FINAL_BOARD]  # Add the initial cell into the queue

    while queue_fb and queue_bf:
        if queue_fb:
            n = queue_fb.pop(0)
            find_open_space(n)
            for node in neighbors(n):
                if node not in visited_fb:
                    print(node)
                    visited_fb.append(node)
                    if(n not in visited_fb):
                        visited_fb.append(n)
                    actions_fb[visited_fb.index(
                        node)] = actions_fb[visited_fb.index(n)] + 1
                    queue_fb.append(node)
                    if node == FINAL_BOARD:
                        print("Done via fb")
                        print(node)
                        print(actions_fb[visited_fb.index(node)])
                        queue_fb.clear()
                        break
        # Back to front
        if queue_bf:
            n = queue_bf.pop(0)
            find_open_space(n)
            for node in neighbors(n):
                if node not in visited_bf:
                    print(node)
                    visited_bf.append(node)
                    if(n not in visited_bf):
                        visited_bf.append(n)
                    actions_bf[visited_bf.index(
                        node)] = actions_bf[visited_bf.index(n)] + 1
                    queue_bf.append(node)
                    if node == FINAL_BOARD:
                        print("Done via bf")
                        print(node)
                        print(actions_bf[visited_bf.index(node)])
                        queue_bf.clear()
                        break
        # n = queue.pop(0)
        # print("\tVisiting ", n)
        # # visited[n] = VISITED
        # for node in neighbors(n, states):
        #     if visited[node[0]][node[1]] == NOT_VISITED:
        #         visited[node[0]][node[1]] = VISITED
        #         actions_fb += 1  # Count the number of actions_fb
        #         queue.append(node)
        #         if board == FINAL_BOARD:
        #             # I'm done!
        #             # Display the number of actions_fb
        #             print(actions_fb)
        #             print("Minimum number of actions_fb ", actions_fb)
        #             # Finish BFS
        #             queue.clear()


bs(board)
