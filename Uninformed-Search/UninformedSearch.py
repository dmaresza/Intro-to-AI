def main():
    print("This script implements Breadth-First and Depth-First Search algorithms\n")
    algorithm = input("Please input bfs or dfs to select which implementation to run: ")
    grid = readGrid("path.txt")
    startLocation = []
    goalLocation = []
    startLocation.append(int(input("Enter row number of start location (between 0-6): ")))
    startLocation.append(int(input("Enter column number of start location (between 0-7): ")))
    goalLocation.append(int(input("Enter row number of goal location (between 0-6): ")))
    goalLocation.append(int(input("Enter column number of goal location (between 0-7): ")))
    expandedNodes, goalNode = uninformedSearch(grid, startLocation, goalLocation, algorithm)
    if(goalNode == None):
        print("No path found between {} and {}".format(startLocation, goalLocation))
    else:
        path = setPath(goalNode, [])
        outputGrid(grid, startLocation, goalLocation, path)
        print("\nPath between {} and {} is: {}".format(startLocation, goalLocation, path))
        print("Path cost is: {}".format(len(path) - 1))
        print("Number of expanded nodes: {}".format(expandedNodes))
        print("Final path written to file pathOutput.txt")
    
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

def uninformedSearch(grid, start, goal, algorithm):
    current = Node(start, None)
    openList = [current]
    closedList = []
    while(len(openList) > 0):
        if(algorithm == "bfs"):
            current = openList.pop(0)
        elif(algorithm == "dfs"):
            current = openList.pop()
        if(current.value == goal):
            return len(closedList), current
        closedList.append(current)
        expandNode(current, grid, openList, closedList)
    return len(closedList), None

def setPath(current, path):
    while(current != None):
        path.insert(0, current.value)
        current = current.parent
    return path
    
def getNeighbors(location, grid):
    neighbors = []
    if(location[0] - 1 >= 0 and grid[location[0] - 1][location[1]] == 0):
        neighbors.append([location[0] - 1, location[1]])
    if(location[1] + 1 < len(grid[0]) and grid[location[0]][location[1] + 1] == 0):
        neighbors.append([location[0], location[1] + 1])
    if(location[0] + 1 < len(grid) and grid[location[0] + 1][location[1]] == 0):
        neighbors.append([location[0] + 1, location[1]])
    if(location[1] - 1 >= 0 and grid[location[0]][location[1] - 1] == 0):
        neighbors.append([location[0], location[1] - 1])
    return neighbors

def expandNode(node, grid, openList, closedList):
    neighbors = getNeighbors(node.value, grid)
    for n in neighbors:
        child = Node(n, node)
        if(not inList(child, openList) and not inList(child, closedList)):
            openList.append(child)

def inList(node, l):
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
    """ Writes a 2D list of integers with spaces in between each character, the starting position marked as "s", the goal position marked as "g", and intermediate points marked with "*" e.g.,
    1 1 1 1 1 
    1 s * * 1
    1 0 0 g 1
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