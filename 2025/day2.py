import re

def solve(pattern, ids):
    res = 0
    for id in ids:
        for i in range(int(id[0]), int(id[1]) + 1):
            if(len(str(i)) == 2 and str(i)[0] == str(i)[1]):
                res += i
            else:
                if(re.search(pattern, str(i))):
                    res += i
    return res

input_file = open("input/day2.txt", "r")
lines = input_file.readlines()
input_file.close()
lines = lines[0].split(',')

ids = []
for i in range(len(lines)):
    ids.append(lines[i].split('-'))
    ids[i][1] = re.sub(r'\b0+(\d+)\b', r'\1', ids[i][1])
    ids[i][0] = re.sub(r'\b0+(\d+)\b', r'\1', ids[i][0].strip())
print(solve(r'^(\d{2,})\1$', ids))
print(solve(r'^(\d+)\1+$', ids))


