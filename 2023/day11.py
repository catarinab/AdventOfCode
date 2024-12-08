f = open("inputs/day11.txt", "r")
lines = f.readlines()
f.close()

spaceIdx = 0
galaxyColumns = [False] * len(lines[0].strip())
galaxies = []
offset = 1000000


#expand rows
for line in lines:
    galaxy = False
    line = line.strip()
    for idx in range(len(line)):
        char = line[idx]
        galaxyColumns[idx] = True if char == '#' else galaxyColumns[idx]
        galaxy = True if char == '#' else galaxy
        if char == '#': galaxies.append((spaceIdx, idx))
    if not galaxy:
        spaceIdx += offset - 1
    spaceIdx += 1

#expand columns
nextGalaxies = [galaxy for galaxy in galaxies]
for idx in range(len(galaxyColumns)):
    if not galaxyColumns[idx]:
        for galIdx in range(len(galaxies)):
            if(galaxies[galIdx][1] > idx):
                nextGalaxies[galIdx] = (nextGalaxies[galIdx][0], nextGalaxies[galIdx][1] + offset - 1)

#manhattan distance
pair = 0
dists = 0
for i1 in range(len(nextGalaxies)):
    for i2 in range(i1 + 1, len(nextGalaxies)):
        dist = abs(nextGalaxies[i1][0] - nextGalaxies[i2][0]) + abs(nextGalaxies[i1][1] - nextGalaxies[i2][1])
        dists += dist
print(dists)
