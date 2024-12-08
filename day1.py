def part1(lines):
    col1, col2 = [], []

    for i in range(len(lines)):
        line = lines[i].split()
        col1.append(int(line[0]))
        col2.append(int(line[1].strip()))

    result = sum(abs(el1 - el2) for el1, el2 in zip(sorted(col1), sorted(col2)))

    print(result)

def part2(lines):
    col1, col2 = [], {}
    similarity = 0

    for i in range(len(lines)):
        line = lines[i].split()
        col1.append(int(line[0]))
        if int(line[1]) in col2:
            col2[int(line[1])] += 1
        else:
            col2[int(line[1])] = 1

    for x in col1:
        if x in col2:
            similarity += x * col2[x]

    print(similarity)

input_file = open("day1.txt", "r")
lines = input_file.readlines()
input_file.close()

part1(lines)    
part2(lines)



