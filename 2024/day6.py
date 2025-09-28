
up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

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
       

def part1(matrix, currentPosition, direction = up, targetPosition=False):
    visitedPositions = []
    while (currentPosition[0] >= 0 and currentPosition[0] < len(matrix) and currentPosition[1] >= 0 and currentPosition[1] < len(matrix[0])):
        if currentPosition == targetPosition and visitedPositions != []:
            return -1

        if matrix[currentPosition[0]][currentPosition[1]] == '#':
            currentPosition = (currentPosition[0] - direction[0], currentPosition[1] - direction[1])
            direction = getNewDirection(direction)
        elif currentPosition not in visitedPositions:
            visitedPositions.append(currentPosition)
        currentPosition = (currentPosition[0] + direction[0], currentPosition[1] + direction[1])
               
    return len(visitedPositions)
    
def part2(matrix, currentPosition):
    currDirection = up
    visitedPositions = []
    visitedBlocks = []
    matrixSize = len(matrix)
    search = False
    while (validPosition(currentPosition, matrixSize)):

        if matrix[currentPosition[0]][currentPosition[1]] == '#':
            currentPosition = (currentPosition[0] - currDirection[0], currentPosition[1] - currDirection[1])
            currDirection = getNewDirection(currDirection)
        elif currentPosition not in visitedPositions:
            visitedPositions.append(currentPosition)
        currentPosition = (currentPosition[0] + currDirection[0], currentPosition[1] + currDirection[1])
        newDirection = getNewDirection(currDirection)
        block = (currentPosition[0] + currDirection[0], currentPosition[1] + currDirection[1])
        relevantCoordinate = getRelevantCoordinate(newDirection)
        for positions in visitedPositions:
            if positions[relevantCoordinate] != block[relevantCoordinate]:
                search = True
                break
        if search:
            search = False
            if  (validPosition(block, matrixSize)) and (matrix[block[0]][block[1]] != '#') and (block not in visitedBlocks) and (block not in visitedPositions) and validPosition(currentPosition, matrixSize) and (matrix[currentPosition[0]][currentPosition[1]] != '#'):
                matrix[block[0]][block[1]] = '#'
                if part1(matrix, currentPosition, newDirection, currentPosition) == -1:
                    visitedBlocks.append(block)
                matrix[block[0]][block[1]] = '.'
    return len(visitedBlocks)

def main():
    input_file = open("input/input.txt", "r")
    inputStrings = input_file.readlines()
    input_file.close()
    matrix = []
    for string in inputStrings:
        line = list(string.strip())
        matrix.append(line)
        if '^' in line:
            startingPoint = (matrix.index(line), line.index('^'))
    print(part1(matrix, startingPoint))
    print(part2(matrix, startingPoint))
    

if __name__ == "__main__":
    main()