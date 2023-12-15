class Pipe:
    def __init__(self, val, coords, prevDir):
        self.val = val
        self.coords = coords
        self.prevDir = prevDir

    def __str__(self):
        return self.val + ": " + str(self.coords) + " " + str(self.prevDir)


dirs = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

possibleDirs = {"|": [dirs["up"], dirs["down"]], "-": [dirs["left"], dirs["right"]], 
                "L": [dirs["right"], dirs["up"]], "J": [dirs["up"], dirs["left"]], 
                "7": [dirs["left"], dirs["down"]], "F": [dirs["right"], dirs["down"]]}


f = open("inputs/day10test.txt", "r")
lines = f.readlines()
f.close()

tiles = []
loop = []
for line in lines: 
    tiles.append([*line.strip()])

for line in tiles:
    for char in line:
        if char == "S":
            coords = (tiles.index(line), line.index(char))
            start = Pipe(char, coords, None)
            loop.append(start)
            

#depth first search?
currTile = loop[0]
adjs = []
for i in range(max(0, coords[0]-1), min(len(tiles[0]), coords[0]+2)):
    pipe = Pipe(tiles[i][coords[1]], (i, coords[1]), (i - coords[0], 0))
    if i != coords[0]:adjs.append(pipe)
for j in range(max(0, coords[1]-1), min(len(tiles), coords[1]+2)):
    pipe = Pipe(tiles[coords[0]][j], (coords[0], j), (0, j -coords[1]))
    if j != coords[1]: adjs.append(pipe)

for start in adjs:
    steps = 0
    currTile = start
    found = False
    while(currTile.val!= "."):
        if(currTile.val == "S"):
            found = True
            break
        if(currTile.val == "."):    
            break
        steps += 1
        prevDir = (currTile.prevDir[0]*-1, currTile.prevDir[1]*-1)
        if(prevDir not in possibleDirs[currTile.val]):
            break
        possibleDir = [i for i in possibleDirs[currTile.val]]
        possibleDir.remove(prevDir)
        coords = (currTile.coords[0] + possibleDir[0][0], currTile.coords[1] + possibleDir[0][1])
        currTile = Pipe(tiles[coords[0]][coords[1]], coords, possibleDir[0])
    if found:
        print(round(steps/2))
        break
