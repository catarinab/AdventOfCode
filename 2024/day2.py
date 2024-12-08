# Description: Advent of Code 2024 - Day 2
class struct():
    def __init__(self):
        self.increasing = False
        self.decreasing = False

debug = False

def part1(level):
    structure = struct()
    for n in range(len(level) - 1):
        diff = level[n] - level[n + 1]

        if (1 <= diff <= 3):
            if(structure.increasing == True):
                return False
            structure.decreasing = True

        elif (-3 <= diff <= -1 ):
            if(structure.decreasing == True):
                return False
            structure.increasing = True

        else:
            return False
    return True

def part2(level, recursive):
    structure = struct()
    for n in range(len(level) - 1):
        diff = level[n] - level[n + 1]

        if (1 <= diff <= 3):
            if(structure.increasing == True):
                return retest(n, level, recursive)
            structure.decreasing = True

        elif (-3 <= diff <= -1 ):
            if(structure.decreasing == True):
                return retest(n, level, recursive)
            structure.increasing = True

        else:
            return retest(n, level, recursive)
    return True

def retest(n, level, recursive):
    if(recursive == True):
        return False
    res1 = False

    level_retry1 = level.copy()
    level_retry1.pop(n)
    res1 = part2(level_retry1, True)
    if(res1):
        return True
    
    level_retry2 = level.copy()
    level_retry2.pop(n + 1)
    res2 = part2(level_retry2, True)
    if(res2):
        return True
    
    if(n == 1):
        level.pop(n - 1)
        return part2(level, True)
    return False


input_file = open("input/day2.txt", "r")
levels = input_file.readlines()
input_file.close()
part1Res, part2Res = 0, 0
for level in levels:
    level = level.split()
    level = [int(x) for x in level]
    
    if(part1(level)):
        part1Res += 1

    if(part2(level, False)):
        part2Res += 1

print("part1Res:", part1Res)
print("part2Res:", part2Res)