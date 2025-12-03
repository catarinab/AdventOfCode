def part1(rots, numbers):
    ptr = 50
    ctr = 0
    for i in range(len(rots)):
        rot = rots[i]
        for j in range(numbers[i]):
            if(rot == 'L'):
                if(ptr == 0):
                    ptr = 99
                else:
                    ptr -= 1
            else:
                if(ptr == 99):
                    ptr = 0
                else:
                    ptr += 1
        if(ptr == 0):
            ctr += 1

    print(ctr)

def part2(rots, numbers):
    ptr = 50
    ctr = 0
    for i in range(len(rots)):
        rot = rots[i]
        for j in range(numbers[i]):
            if(rot == 'L'):
                if(ptr == 0):
                    ptr = 99
                else:
                    ptr -= 1
            else:
                if(ptr == 99):
                    ptr = 0
                else:
                    ptr += 1
            if(ptr == 0):
                ctr += 1

    print(ctr)


input_file = open("input/day1.txt", "r")
lines = input_file.readlines()
input_file.close()

col1 = []
col2 = []
for i in range(len(lines)):
    col1.append(lines[i][0])
    col2.append(int(lines[i][1:].strip()))

part1(col1, col2)
part2(col1, col2)

