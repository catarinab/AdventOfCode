f = open("inputs/day5.txt", "r")
lines = f.readlines()
f.close()

class Mapping:
    def __init__(self, begin, end, beginMapping):
        self.begin = begin
        self.end = end
        self.beginMapping = beginMapping

seeds = [int(i) for i in lines[0].split(":")[1].split()]

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
for seed in seeds:
    currMapping = seed
    for i in range(7):
        currList = mappings[i]
        for mapping in currList:
            if(currMapping >= mapping.begin and currMapping <= mapping.end):
                currMapping = mapping.beginMapping + (currMapping - mapping.begin)
                break
    locations.append(currMapping)
    print("Seed: " + str(seed) + " -> " + str(currMapping))
print(min(locations))
