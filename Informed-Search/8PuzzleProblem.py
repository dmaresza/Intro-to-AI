import heapq

def main():
    print("This script implements the A* algorithm on the 8-puzzle problem\n"
        "\nThe initial state is read from file 8PuzzleStart.txt\n"
        "The goal state is read from file 8PuzzleGoal.txt")
    startState = readGrid("8PuzzleStart.txt")
    goalState = readGrid("8PuzzleGoal.txt")
    print("\nInitial State:\n" + '\n'.join([' '.join(['{}'.format(item) for item in row]) for row in startState]))
    print("\nGoal State:\n" + '\n'.join([' '.join(['{}'.format(item) for item in row]) for row in goalState]))
    expandedStates, finalState = informedSearch(startState, goalState)
    if finalState == None:
        print("No path found between Initial State and Goal State")
    else:
        path = setPath(finalState, [])
        print("\nPath between Initial State and Goal State is:\n" + 
        '\n\n'.join(['\n'.join([' '.join(['{}'.format(item) for item in row]) for row in state]) for state in path]))
        print("\nPath cost is: {}".format(finalState.g))
        print("Number of explored states: {}".format(expandedStates))
        print("Heuristic function used: Manhattan Distance")

def readGrid(filename):
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
    f.close()
    return grid

'''If no path can be found, program takes hours to search
through all 181,440 possible states, so I added a stop
condition after 15,000 explored states because no possible
solution will take that long to find'''
def informedSearch(start, goal):
    current = Board(start, None, 0, getHeuristic(start, goal))
    openList = []
    heapq.heappush(openList, current)
    closedList = []
    while len(openList) > 0:
        current = heapq.heappop(openList)
        if current.value == goal:
            return len(closedList), current
        closedList.append(current)
        if len(closedList) > 15000:
            break;
        expandState(current, openList, closedList, goal)
    return len(closedList), None

def setPath(current, path):
    while current != None:
        path.insert(0, current.value)
        current = current.parent
    return path

def getHeuristic(start, goal):
    hCost = 0
    for i in range(1, 9):
        for r in range(len(start)):
            for c in range(len(start[0])):
                if i == start[r][c]:
                    startPosition = [r, c]
                if i == goal[r][c]:
                    goalPosition = [r, c]
        hCost += abs(goalPosition[0] - startPosition[0]) + abs(goalPosition[1] - startPosition[1])
    return hCost

def expandState(board, openList, closedList, goal):
    neighbors = getNeighborStates(board.value)
    #print("Neighbor states:\n" + '\n\n'.join(['\n'.join([' '.join(['{}'.format(item) for item in row]) for row in state]) for state in neighbors]))
    for n in neighbors:
        child = Board(n, board, board.g + 1, getHeuristic(n, goal))
        inOpenList, existingState = inList(child, openList)
        inClosedList, temp = inList(child, closedList)
        if inOpenList:
            if child.g < existingState.g:
                openList.remove(existingState)
                heapq.heappush(openList, child)
                if inClosedList:
                    closedList.remove(existingState)
        elif not inClosedList:
            heapq.heappush(openList, child)

def getNeighborStates(state):
    neighborStates = []
    for r in range(len(state)):
        for c in range(len(state[0])):
            if state[r][c] == 0:
                zeroPos = [r, c]
    if(zeroPos[0] - 1 >= 0):
        tempState1 = []
        for r in state:
            tempState1.append(r.copy())
        tempState1[zeroPos[0]][zeroPos[1]] = tempState1[zeroPos[0] - 1][zeroPos[1]]
        tempState1[zeroPos[0] - 1][zeroPos[1]] = 0
        neighborStates.append(tempState1)
    if(zeroPos[1] + 1 < len(state[0])):
        tempState2 = []
        for r in state:
            tempState2.append(r.copy())
        tempState2[zeroPos[0]][zeroPos[1]] = tempState2[zeroPos[0]][zeroPos[1] + 1]
        tempState2[zeroPos[0]][zeroPos[1] + 1] = 0
        neighborStates.append(tempState2)
    if(zeroPos[0] + 1 < len(state)):
        tempState3 = []
        for r in state:
            tempState3.append(r.copy())
        tempState3[zeroPos[0]][zeroPos[1]] = tempState3[zeroPos[0] + 1][zeroPos[1]]
        tempState3[zeroPos[0] + 1][zeroPos[1]] = 0
        neighborStates.append(tempState3)
    if(zeroPos[1] - 1 >= 0):
        tempState4 = []
        for r in state:
            tempState4.append(r.copy())
        tempState4[zeroPos[0]][zeroPos[1]] = tempState4[zeroPos[0]][zeroPos[1] - 1]
        tempState4[zeroPos[0]][zeroPos[1] - 1] = 0
        neighborStates.append(tempState4)
    return neighborStates

def inList(state, l):
    for s in l:
        if state.value == s.value:
            return True, s
    return False, None

class Board:
    def __init__(self, value, parent, pathCost, heuristicCost):
        self.value = value
        self.parent = parent
        self.g = pathCost
        self.h = heuristicCost
        self.f = self.g + self.h
    
    def __lt__(self, other):
        return self.f < other.f

if __name__ == '__main__':
    main()