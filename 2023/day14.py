def checkCondition(coord, dir, nextLocation, grid):
    if((coord == 0 and dir == -1) or (coord == 1 and dir == -1)):
        return nextLocation[coord] >= 0
    elif(coord == 0 and dir == 1):
        return nextLocation[coord] < len(grid)
    elif(coord == 1 and dir == 1):
        return nextLocation[coord] < len(grid[0])

def rollStone(stone, grid, coord, dir):
    nextLocation = [stone[0], stone[1]]
    nextLocation[coord] += dir
    while(checkCondition(coord, dir, nextLocation, grid)):
        if(grid[nextLocation[0]][nextLocation[1]] == '#' or grid[nextLocation[0]][nextLocation[1]] == 'O'):
            nextLocation[coord] -= dir
            return nextLocation
        nextLocation[coord] += dir
    nextLocation[coord] -= dir
    return nextLocation

def sortByCoord(stoneLocations, coord, reverse):
    return sorted(stoneLocations, key=lambda x: x[coord], reverse=reverse)



f = open("/home/cat/uni/aoc23/inputs/day14.txt", "r")
lines = f.readlines()
f.close()

grid = []
stoneLocations = []
nrCycles = 1000 #uh
dirs = [(0,-1), (1,-1), (0,1), (1,1)]

for lineIdx in range(len(lines)):
    line = lines[lineIdx].replace('\n', '')
    grid.append([*line])
    for charIdx in range(len(line)):
        if(line[charIdx] == 'O'):
            stoneLocations.append((lineIdx, charIdx))

sum = 0
totalCols = len(grid)
for _ in range(nrCycles):
    for dir in dirs:
        sum = 0
        newLocations = []
        stoneLocations = sortByCoord(stoneLocations, dir[0], reverse= (dir[1] == 1))
        for stone in stoneLocations:
            newLocation = rollStone(stone, grid, dir[0], dir[1])
            grid[stone[0]][stone[1]] = '.'
            grid[newLocation[0]][newLocation[1]] = 'O'
            newLocations.append(newLocation)
            sum += totalCols - (newLocation[0])
        stoneLocations = [i for i in newLocations]

print(sum)
