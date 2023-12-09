f = open("inputs/day3.txt", "r")
lines = f.readlines()
f.close()

symbols = ['#', '$', '*', '+', '-', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '&', '%']

sum = 0

def processNum(begin, end, line, k):
    adjs.append(line[begin - 1])
    if end != len(line) - 1:
        adjs.append(line[end + 1])

    adjBegin = 0 if begin == 0 else begin - 1
    if(end == len(line) - 1):
        adjEnd = len(line)
    elif(end == len(line) - 2):
        adjEnd = len(line) - 1
    else:
        adjEnd = end + 2
    if k != 0:
        for index in range(adjBegin, adjEnd):
            adjs.append(lines[k - 1][index])

    if k != len(lines) - 1:
        for index in range(adjBegin, adjEnd):
            adjs.append(lines[k + 1][index])
    if(not set(adjs).isdisjoint(symbols)):
        return int("".join(line[begin:end + 1]))
    else:
        return 0

for k in range(len(lines)):
    line = lines[k]
    line = line.strip()
    line = [i for i in line if i]
    begin = -1
    end = -1
    adjs = []

    for i in range(len(line)):
        if line[i].isnumeric():
            if(begin == -1):
                begin = i
                end = i
            else:
                end = i
        elif(begin != -1):
            sum += processNum(begin, end, line, k)
            begin = -1
            end = -1
            adjs = []
    if(begin != -1):
        sum += processNum(begin, end, line, k)

print(sum)