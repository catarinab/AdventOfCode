f = open("/home/cat/uni/aoc23/inputs/day15.txt", "r")
lines = f.readlines()
f.close()

steps = []

def algorithm(step):
    val = 0
    for char in step:
        val += ord(char)
        val *= 17
        val = val % 256
    return val


val = 0
line = lines[0].split(',')
for el in line:
    val += algorithm(el)

print(val)