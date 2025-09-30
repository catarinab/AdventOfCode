
up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)

matrix = []
visitedDirections = dict()
visitedPositions = []

directions = [up, right, down, left]

#always turn right
def getNewDirection(direction):
    if direction == up:
        return right
    elif direction == right:
        return down
    elif direction == down:
        return left
    return up
    
    
def validPosition(position, matrixSize):
    return position[0] >= 0 and position[0] < matrixSize and position[1] >= 0 and position[1] < matrixSize
       

def part1(position, direction = up):
    matrixSize = len(matrix)
    while (validPosition(position, matrixSize)):  
        if matrix[position[0]][position[1]] == '#':
            position = (position[0] - direction[0], position[1] - direction[1])
            direction = getNewDirection(direction)
            continue
        if position not in visitedPositions:
            visitedPositions.append(position)
        if(position not in visitedDirections):
            visitedDirections[position] = direction 
        position = (position[0] + direction[0], position[1] + direction[1])
    return len(visitedPositions)
    
    

def findLoop(position, direction, targetPosition):
    matrixSize = len(matrix)
    directions = dict()
    while (validPosition(position, matrixSize)):
        if matrix[position[0]][position[1]] == '#':
            position = (position[0] - direction[0], position[1] - direction[1])
            direction = getNewDirection(direction)
            continue
        if position in directions and direction in directions[position]:
            return True
        if(position not in directions):
            directions[position] = [direction]
        else:
            directions[position].append(direction)
        position = (position[0] + direction[0], position[1] + direction[1])

    return False

def part2(startingPoint):
    visitedBlocks = []
    search = False
    matrixSize = len(matrix)
    
    for block in visitedDirections:
        if(block == startingPoint):
            continue
        direction = visitedDirections[block]
        newPosition = (block[0] - direction[0], block[1] - direction[1])
        newDirection = getNewDirection(direction)
        matrix[block[0]][block[1]] = "#"
        loop = findLoop(newPosition, newDirection, newPosition)
        matrix[block[0]][block[1]] = "."
        if(loop):
            visitedBlocks.append(block)
    return len(visitedBlocks)
      

def main():
    input_file = open("input/input.txt", "r")
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