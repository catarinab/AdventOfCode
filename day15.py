def algorithm(step):
    val = 0
    for char in step:
        val += ord(char)
        val *= 17
        val = val % 256
    return val

def addLens(lens, index):
    lens = lens.split('=')
    for item in boxes[index]:
        if item[0] == lens[0]:
            item[1] = int(lens[1])
            return
    boxes[index].append(lens)

def removeLens(lens, index):
    lens = lens[0:-1]
    for item in boxes[index]:
        if item[0] == lens:
            boxes[index].remove(item)
            return

f = open("inputs/day15.txt", "r")
lines = f.readlines()
f.close()

boxes = []
for i in range(256):
    boxes.append([])

val = 0
line = lines[0].split(',')
for el in line:
    limit = -1 if el[-1] == '-' else -2
    index = algorithm(el[0:limit])
    print(el, index)
    if(el[-1] == '-'):
        removeLens(el, index)
    else:
        addLens(el, index)

sum = 0
for boxIdx in range(len(boxes)):
    for lensIdx in range(len(boxes[boxIdx])):
        sum += (boxIdx + 1) * (lensIdx + 1) * int(boxes[boxIdx][lensIdx][1])

print(sum)