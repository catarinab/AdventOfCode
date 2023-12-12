from math import lcm

class mapping:
    def __init__(self, loc, left, right):
        self.loc = loc
        self.left = left
        self.right = right
        

f = open("inputs/day8test.txt", "r")
lines = f.readlines()
f.close()

directions = [*lines[0].split()[0]]

print(directions)

mappings = {}
beginnings = []

#processing
for idx in range(2, len(lines)):
    line = lines[idx].split(" = (")
    id = line[0]
    line = line[1].strip(")\n")
    line = line.split(",")
    mappings[id] = mapping(id, line[0], line[1].strip(" "))
    if(id[2] == "A"):
        beginnings.append(id)
print(mappings)
print(beginnings)

dirIdx = 0
stepVals = []
steps = 0
for location in beginnings:
    steps = 0
    while(location[2] != "Z"):
        dir = directions[dirIdx];
        location = mappings[location]
        location = location.left if dir == "L" else location.right
        dirIdx = (dirIdx + 1) % len(directions)
        steps += 1
    stepVals.append(steps)

for i in range(len(stepVals)):
    print(stepVals[i])

#uh...
print(lcm(stepVals[0], stepVals[1], stepVals[2], stepVals[3], stepVals[4], stepVals[5]))
