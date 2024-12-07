import re

do = True

pattern = r"M.S.A.M.S|S.M.A.S.M|M.M.A.S.S|S.S.A.M.M"
matches = 0

input_file = open("input/day4.txt", "r")
inputStrings = input_file.readlines()

#find x-mas

#get all 3x3 grids
for i in range(len(inputStrings) - 2):
    for j in range(len(inputStrings[0]) - 3):
        grid = ""
        for k in range(3):
            grid += inputStrings[i + k][j:j + 3].strip()
        matches += len(re.findall(pattern, grid))

print(matches)