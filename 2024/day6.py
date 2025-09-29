
up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

matrix = []
visitedDirections = dict()
visitedPositions = []

directions = [up, right, down, left]

def getRelevantCoordinate(direction):
    if(direction == up or direction == down):
        return 0
    return 1

#always turn right
def getNewDirection(currentDirection):
    if currentDirection == up:
        return right
    elif currentDirection == right:
        return down
    elif currentDirection == down:
        return left
    return up
    
    
def validPosition(position, matrixSize):
    return position[0] >= 0 and position[0] < matrixSize and position[1] >= 0 and position[1] < matrixSize
       

def part1(currentPosition, direction = up):
    matrixSize = len(matrix)
    while (validPosition(currentPosition, matrixSize)):  
        currentPosition = (currentPosition[0] + direction[0], currentPosition[1] + direction[1])
        if not validPosition(currentPosition, matrixSize):
            break
        if matrix[currentPosition[0]][currentPosition[1]] == '#':
            currentPosition = (currentPosition[0] - direction[0], currentPosition[1] - direction[1])
            direction = getNewDirection(direction)
        else:
            if currentPosition not in visitedPositions:
                visitedPositions.append(currentPosition)
            if(currentPosition not in visitedDirections):
                visitedDirections[currentPosition] = direction      
    print(visitedPositions)
    return len(visitedPositions)
    
    

def findLoop(currentPosition, direction, targetPosition):
    matrixSize = len(matrix)
    while (currentPosition[0] >= 0 and currentPosition[0] < matrixSize and currentPosition[1] >= 0 and currentPosition[1] < matrixSize):
        if matrix[currentPosition[0]][currentPosition[1]] == '#':
            currentPosition = (currentPosition[0] - direction[0], currentPosition[1] - direction[1])
            direction = getNewDirection(direction)
        currentPosition = (currentPosition[0] + direction[0], currentPosition[1] + direction[1])
        if currentPosition == targetPosition:
            return True
    return False

def part2(startingPoint):
    currDirection = up
    visitedBlocks = []
    search = False
    matrixSize = len(matrix)
    
    print(visitedDirections)
    
    for block in visitedDirections:
        if(block == startingPoint):
            continue
        direction = visitedDirections[block]
        newPosition = (block[0] - direction[0], block[1] - direction[1])
        newDirection = getNewDirection(direction)
        print("initializing block: ", block)
        loop = findLoop(newPosition, newDirection, newPosition)
        print("finished block: ", block)
        if(loop):
            visitedBlocks.append(block)
        
    print(visitedBlocks)
    return len(visitedBlocks)
      

def main():
    input_file = open("input/sexample.txt", "r")
    inputStrings = input_file.readlines()
    input_file.close()
    for string in inputStrings:
        line = list(string.strip())
        matrix.append(line)
        if '^' in line:
            startingPoint = (matrix.index(line), line.index('^'))
    print(part1(startingPoint))
    print(part2(startingPoint))
    

if __name__ == "__main__":
    main()