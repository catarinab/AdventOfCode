import re

do = True

pattern = r"mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\)"
result = 0

input_file = open("input/day3.txt", "r")
inputStrings = input_file.readlines()

for inputString in inputStrings:
    matches = re.finditer(pattern, inputString)
    results = [match.group() for match in matches]
    multiplications = re.findall(pattern, inputString)
    for index in range(len(multiplications)):
        if(results[index] == "do()"):
            do = True
            continue
        if(results[index] == "don't()"):
            do = False
            continue
        if(do):
            result += int(multiplications[index][0]) * int(multiplications[index][1])

print(result)