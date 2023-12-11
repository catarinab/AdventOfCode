f = open("/home/cat/uni/aoc23/inputs/day5.txt", "r")
lines = f.readlines()
f.close()

class Mapping:
    def __init__(self, begin, end, beginMapping):
        self.begin = begin
        self.end = end
        self.beginMapping = beginMapping

def checkRange(seedPair, mapping):
    start = max(seedPair[0], mapping.begin)
    end = min(seedPair[0] + seedPair[1] - 1, mapping.end)
    if(start > end): return [], []
    offset = mapping.beginMapping - mapping.begin
    result = (start + offset, end - start + 1)
    rest = []
    if(start > seedPair[0]): rest.append((seedPair[0], start - seedPair[0]))
    if(end < seedPair[0] + seedPair[1] - 1): rest.append((end + 1, seedPair[0] + seedPair[1] - end - 1))
    return result, rest





seeds = [int(i) for i in lines[0].split(":")[1].split()]
seedPairs = []
for i in range(0,len(seeds), 2):
    seedPairs.append((seeds[i], seeds[i+1]))

soil = []
fertilizer = []
water = []
light = []
temperature = []
humidity = []
location = []



#Mappings
mappings = {0: soil, 1: fertilizer, 2: water, 3: light, 4: temperature, 5: humidity, 6: location}
currMap = -1
lineIdx = 2
while(lineIdx < len(lines)):
    currLine = lines[lineIdx].split(" ")
    if(not currLine[0].isnumeric() and currLine[0] != "\n"):
        currMap += 1
    elif(currLine[0].isnumeric()):
        currLine = [int(i) for i in currLine]
        begin = currLine[1]
        beginMapping = currLine[0]
        forRange = currLine[2]
        mappings[currMap].append(Mapping(begin, begin + forRange - 1, beginMapping))
    
    lineIdx += 1



locations = []

for seedPair in seedPairs:
    nextRanges = [seedPair]
    for i in range(7):
        seedLists = [i for i in nextRanges]
        nextRanges = []

        while(len(seedLists) > 0):
            currList = mappings[i]
            currMapping = seedLists.pop(0)
            found = False
            if(currMapping[1] == 0): continue
            for mapping in currList:
                result, rest = checkRange(currMapping, mapping)
                if(result != []): 
                    found = True
                    nextRanges.append(result)
                    if(rest != []): 
                        [seedLists.append(i) for i in rest]
                    break
            if(not found):
                nextRanges.append(currMapping)
    [locations.append(i[0]) for i in nextRanges]

print(min(locations))
    

