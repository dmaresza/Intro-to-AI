import heapq
import math

def main():
    print("This script implements A* and Greedy Search algorithms\n")
    algorithm = input("Please input astar or greedy to select which implementation to run: ")
    grid = readGrid("path.txt")
    startLocation = []
    goalLocation = []
    startLocation.append(int(input("Enter row number of start location (between 0-9): ")))
    startLocation.append(int(input("Enter column number of start location (between 0-9): ")))
    goalLocation.append(int(input("Enter row number of goal location (between 0-9): ")))
    goalLocation.append(int(input("Enter column number of goal location (between 0-9): ")))
    expandedNodes, goalNode = informedSearch(grid, startLocation, goalLocation, algorithm)
    if(goalNode == None):
        print("No path found between {} and {}".format(startLocation, goalLocation))
    else:
        path = setPath(goalNode, [])
        outputGrid(grid, startLocation, goalLocation, path)
        print("\nPath between {} and {} is: {}".format(startLocation, goalLocation, path))
        print("Path cost is: {}".format(goalNode.g))
        print("Number of expanded nodes: {}".format(expandedNodes))
        print("Heuristic function used: Straight-line distance")
        print("Final path written to file pathOutput.txt")
    
class Node:
    def __init__(self, value, parent, pathCost, heuristicCost, algorithm):
        self.value = value
        self.parent = parent
        self.g = pathCost
        self.h = heuristicCost
        if(algorithm == 'greedy'):
            self.f = self.h
        elif(algorithm == 'astar'):
            self.f = self.g + self.h
    
    def __lt__(self, other):
        return self.f < other.f

def informedSearch(grid, start, goal, algorithm):
    current = Node(start, None, 0, math.dist(start, goal), algorithm)
    openList = []
    heapq.heappush(openList, current)
    closedList = []
    while(len(openList) > 0):
        current = heapq.heappop(openList)
        if(current.value == goal):
            return len(closedList), current
        closedList.append(current)
        expandNode(current, grid, openList, closedList, goal, algorithm)
    return len(closedList), None

def setPath(current, path):
    while(current != None):
        path.insert(0, current.value)
        current = current.parent
    return path
    
def getNeighbors(location, grid):
    neighbors = []
    if(location[0] - 1 >= 0 and grid[location[0] - 1][location[1]] != 0):
        neighbors.append([location[0] - 1, location[1]])
    if(location[1] + 1 < len(grid[0]) and grid[location[0]][location[1] + 1] != 0):
        neighbors.append([location[0], location[1] + 1])
    if(location[0] + 1 < len(grid) and grid[location[0] + 1][location[1]] != 0):
        neighbors.append([location[0] + 1, location[1]])
    if(location[1] - 1 >= 0 and grid[location[0]][location[1] - 1] != 0):
        neighbors.append([location[0], location[1] - 1])
    return neighbors

def expandNode(node, grid, openList, closedList, goalLocation, algorithm):
    neighbors = getNeighbors(node.value, grid)
    for n in neighbors:
        child = Node(n, node, grid[n[0]][n[1]] + node.g, math.dist(n, goalLocation), algorithm)
        isInOpenList, existingNode = inOpenList(child, openList)
        if isInOpenList and child.g < existingNode.g:
            openList.remove(existingNode)
            heapq.heappush(openList, child)
            if inClosedList(existingNode, closedList):
                closedList.remove(existingNode)
        elif not inClosedList(child, closedList):
            heapq.heappush(openList, child)
        '''
        isInOpenList, temp = inList(child, openList)
        isInClosedList, temp = inList(child, closedList)
        if not isInOpenList and not isInClosedList:
            heapq.heappush(openList, child)
        if(not inList(child, openList) and not inClosedList(child, closedList)):
            heapq.heappush(openList, child)'''

def inOpenList(node, l):
    for e in l:
        if node.value == e.value:
            return True, e
    return False, None

def inClosedList(node, l):
    for e in l:
        if node.value == e.value:
            return True
    return False

def readGrid(filename):
    """ Reads a grid from a file and returns it as a 2D list. The grid values must be separated by spaces, e.g.,
    1 1 1 1 1 
    1 0 0 0 1
    1 0 0 0 1
    1 1 1 1 1
 
    Args:
        filename (string): the filename to read from
    Return:
        grid: 2D list where each cell stores the value of the grid at that location
    """
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
    
    f.close()
    #print 'Exiting readGrid'
    return grid

def outputGrid(grid, start, goal, path):
    """ Writes a 2D list of integers with spaces in between each character, the starting position marked as "S", the goal position marked as "G", and intermediate points marked with "*" e.g.,
    1 1 1 1 1 
    1 S * * 1
    1 0 0 G 1
    1 1 1 1 1
 
    Args:
        grid (2D list): the grid to write
        start (list): starting position (row, column)
        goal (list): goal position (row, column)
    """
    #print('In outputGrid')
    filenameStr = 'pathOutput.txt'
 
    # Open filename
    f = open(filenameStr, 'w')
 
    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'
 
    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1:
            grid[p[0]][p[1]] = '*'
 
    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            
            # Don't add a ' ' at the end of a line
            if c < len(row)-1:
                f.write(str(col)+' ')
            else:
                f.write(str(col))
 
        # Don't add a '\n' after the last line
        if r < len(grid)-1:
            f.write("\n")
 
    # Close file
    f.close()
    #print('Exiting outputGrid')

if __name__ == '__main__':
    main()