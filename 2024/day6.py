
up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

directions = [up, right, down, left]


#always turn right
def getNewDirection(currentDirection):
    if currentDirection == up:
        return right
    elif currentDirection == right:
        return down
    elif currentDirection == down:
        return left
    elif currentDirection == left:
        return up
       

def part1(matrix, currentPosition):
    currDirection = up
    visitedPositions = []
    while (currentPosition[0] >= 0 and currentPosition[0] < len(matrix) 
           and currentPosition[1] >= 0 and currentPosition[1] < len(matrix[0])):

        if matrix[currentPosition[0]][currentPosition[1]] == '#':
            currentPosition = (currentPosition[0] - currDirection[0], currentPosition[1] - currDirection[1])
            currDirection = getNewDirection(currDirection)
        elif currentPosition not in visitedPositions:
            visitedPositions.append(currentPosition)
        currentPosition = (currentPosition[0] + currDirection[0], currentPosition[1] + currDirection[1])
    return len(visitedPositions)
    
def part2(matrix, currentPosition):
    currDirection = up
    visitedPositions = []
    visitedBlocks = []
    while (currentPosition[0] >= 0 and currentPosition[0] < len(matrix) 
           and currentPosition[1] >= 0 and currentPosition[1] < len(matrix[0])):

        if matrix[currentPosition[0]][currentPosition[1]] == '#':
            currentPosition = (currentPosition[0] - currDirection[0], currentPosition[1] - currDirection[1])
            currDirection = getNewDirection(currDirection)
        elif currentPosition not in visitedPositions:
            visitedPositions.append(currentPosition)
        currentPosition = (currentPosition[0] + currDirection[0], currentPosition[1] + currDirection[1])
        newDirection = getNewDirection(currDirection)
        print(currentPosition, newDirection)
        newPosition = (currentPosition[0] + newDirection[0], currentPosition[1] + newDirection[1])
        if(newPosition in visitedPositions):
            print(newPosition)
            block = (currentPosition[0] + currDirection[0], currentPosition[1] + currDirection[1])
            if block not in visitedBlocks:
                visitedBlocks.append(block)
                print(visitedBlocks)
    return len(visitedPositions)

def main():
    input_file = open("input/example.txt", "r")
    inputStrings = input_file.readlines()
    input_file.close()
    matrix = []
    for string in inputStrings:
        line = list(string.strip())
        matrix.append(line)
        if '^' in line:
            startingPoint = (matrix.index(line), line.index('^'))
    #print(part1(matrix, startingPoint))
    print(part2(matrix, startingPoint))
    

if __name__ == "__main__":
    main()