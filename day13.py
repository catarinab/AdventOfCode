class Mapping():
    def __init__(self, colsLength):
        self.lines = []
        self.cols = []
        for _ in range(colsLength):
            self.cols.append("")
    
def processPatternLines(idx, pattern):
    idx1 = idx - 1
    idx2 = idx
    while(idx1 > -1 and idx2 < len(pattern.lines) ):
        if(pattern.lines[idx1] != pattern.lines[idx2]):
            return False
        idx1 -= 1; idx2 += 1
    return True

def processPatternColumns(idx, pattern):
    idx1 = idx - 1
    idx2 = idx
    while(idx1 > -1 and idx2 < len(pattern.cols)):
        if(pattern.cols[idx1] != pattern.cols[idx2]):
            return False
        idx1 -= 1; idx2 += 1
    return True

def processPattern(pattern):
    for idx in range(1, len(pattern.lines)):
        if(processPatternLines(idx, pattern)):
            return (idx)*100
    
    for idx in range(1, len(pattern.cols)):
        if(processPatternColumns(idx, pattern)):
            return (idx)
    return False

f = open("/home/cat/uni/aoc23/inputs/day13.txt", "r")
lines = f.readlines()
f.close()

mapping = Mapping(len(lines[0])-1)
maps = []

for idx in range(len(lines)):
    lines[idx] = lines[idx].replace('\n', '')

    if(lines[idx] != ''):
        mapping.lines.append(lines[idx])
        for i in range(len(lines[idx])):
            mapping.cols[i] += lines[idx][i]

    if(lines[idx] == '' or idx == len(lines)-1):
        maps.append(mapping)
        mapping = Mapping(len(lines[(idx+1)%len(lines)])-1)

sum = 0
lineIdx = -1
for pattern in maps:
    sum += processPattern(pattern)
print(sum)