#A* Algorithm

GoalNode = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Start
# StartNode = [[2, 8, 1],
#              [4, 7, 3],
#              [0, 6, 5]]  # Goal
StartNode = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
distance = []  # list for distances

# manhattan distance
h1 = -1  # number of misplaced cells
h2 = 0

print("StartNode", StartNode)
print("GoalNode", GoalNode)

for i in range(len(StartNode)):
    for j in range(len(StartNode)):
        if StartNode[i][j] != GoalNode[i][j]:
            h1 += 1  # add 1 everytime a cell is misplaced


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
                # no other positions possible in a 3x3 Puzzle
                print("this is not an 8-puzzle")

for i in range(len(distance)):
    h2 += distance[i]  # sum of distances

print("\nDistance of the cells form their goals position:", distance)
print("\nAmout of Misplaced cells:", h1)
print("\nDistances:", h2)
cost = h1 + h2  # Costs/ Steps to achieve goaldboard
print("\nSteps to achieve Goalboard:", cost)
