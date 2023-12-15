class Mapping():
    def __init__(self, id, mapping):
        self.id = id
        self.extrapolations = [mapping]
    
    def __str__(self):
        return self.id + ": " + str(self.extrapolations)

f = open("inputs/day9.txt", "r")
lines = f.readlines()
f.close()

mappings = []

for line in lines:
    line = line.split();
    vals = [int(x) for x in line]
    mappings.append(Mapping(line[0], vals))

firstSum = 0
secondSum = 0
for idx in range(len(mappings)):
    notFound = True
    currMapping = mappings[idx].extrapolations[0]
    while(notFound):
        currSum = 0
        newExtrapolation = []
        for i in range(len(currMapping)-1):
            diff = currMapping[i+1] - currMapping[i]
            currSum += abs(diff)
            newExtrapolation.append(diff)
        mappings[idx].extrapolations.append(newExtrapolation)
        notFound = currSum != 0
        currMapping = mappings[idx].extrapolations[-1]

    for i in range(len(mappings[idx].extrapolations)-1, 0, -1):
        mappings[idx].extrapolations[i-1].append(mappings[idx].extrapolations[i-1][-1] + mappings[idx].extrapolations[i][-1])
        mappings[idx].extrapolations[i-1].insert(0, mappings[idx].extrapolations[i-1][0] - mappings[idx].extrapolations[i][0])
    firstSum += mappings[idx].extrapolations[0][-1]
    secondSum += mappings[idx].extrapolations[0][0]

print(firstSum)
print(secondSum)
    

