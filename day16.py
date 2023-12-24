dirs = {"right": (0,1), "left": (0,-1), "down": (1,0), "up": (-1,0)}
grid = []

def processMirror(dir, mirror):
    if mirror == '/':
        if dir == dirs["right"]: return dirs["up"]

        elif dir == dirs["left"]: return dirs["down"]

        elif dir == dirs["down"]: return dirs["left"]

        elif dir == dirs["up"]:  return dirs["right"]
    elif mirror == '\\':
        if dir == dirs["right"]:  return dirs["down"]

        elif dir == dirs["left"]: return dirs["up"]

        elif dir == dirs["down"]:  return dirs["right"]

        elif dir == dirs["up"]: return dirs["left"]

def processSplinters(dir, splinter):
    if splinter == '|':
        if (dir == dirs["up"] or dir == dirs["down"]): return dir, None
        else:
            return dirs["up"], dirs["down"]
    if splinter == '-':
        if (dir == dirs["left"] or dir == dirs["right"]): return dir, None
        else:
            return dirs["left"], dirs["right"]

def processGrid(currCoord, dir, energizedCoords = [], energizedPoints = [], loop = 0):
    while (currCoord[0] >= 0 and currCoord[0] < len(grid) and currCoord[1] >= 0 and currCoord[1] < len(grid[0])):
        loop += 1
        if (loop > 1000): return energizedCoords, energizedPoints
        if([currCoord, dir] in energizedPoints):
            return energizedCoords, energizedPoints, [currCoord[0] - dir[0], currCoord[1] - dir[1]]

        energizedPoints.append([currCoord, dir])
        if currCoord not in energizedCoords: energizedCoords.append(currCoord)

        if grid[currCoord[0]][currCoord[1]] == '/' or  grid[currCoord[0]][currCoord[1]] == '\\':
            dir = processMirror(dir, grid[currCoord[0]][currCoord[1]])

        elif grid[currCoord[0]][currCoord[1]] == '|' or grid[currCoord[0]][currCoord[1]] == '-':
            dir, dir2 = processSplinters(dir, grid[currCoord[0]][currCoord[1]])
            if dir2 != None: energizedCoords, energizedPoints, _ = \
                processGrid((currCoord[0] + dir2[0], currCoord[1] + dir2[1]), dir2, 
                            energizedCoords, energizedPoints, loop)

        currCoord = (currCoord[0] + dir[0], currCoord[1] + dir[1])
    return energizedCoords, energizedPoints, [currCoord[0] - dir[0], currCoord[1] - dir[1]]


def main():
    maxEnergy = 0
    f = open("inputs/day16.txt", "r")
    lines = f.readlines()
    f.close()
    exits = []

    for line in lines:
        grid.append([*line.replace('\n', '')])

    #top right corner
    for i in range(len(grid[0])):
        print(exits)
        if (0,i) not in exits:
            temp1, _, exitTile1 = processGrid((0,i), dirs["down"], [], [])
            maxEnergy = max(maxEnergy, len(temp1))
            exits.append(exitTile1)

        if (len(grid) - 1, i) not in exits:
            temp2, _, exitTile2 = processGrid((len(grid) - 1, i), dirs["up"], [], [])
            maxEnergy = max(maxEnergy, len(temp2))
            exits.append(exitTile2)

    for i in range(len(grid)):
        print(exits)
        if (i, 0) not in exits:
            temp1, _, exitTile1 = processGrid((i, 0), dirs["right"], [], [])
            maxEnergy = max(maxEnergy, len(temp1))
            exits.append(exitTile1)
        
        if (i, len(grid[0]) - 1) not in exits:
            temp2, _, exitTile2 = processGrid((i, len(grid[0]) - 1), dirs["left"], [], [])
            maxEnergy = max(maxEnergy, len(temp2))
            exits.append(exitTile2)
    print(maxEnergy)

if __name__ == '__main__':
    main()