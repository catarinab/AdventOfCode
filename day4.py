import re

do = True

pattern = r'(?=(XMAS|SAMX))'
matches = 0

input_file = open("input/day4.txt", "r")
inputStrings = input_file.readlines()

#find xmas in lines
for n in range(len(inputStrings)):
    inputStrings[n] = inputStrings[n].strip()
    matches += len(re.findall(pattern, inputStrings[n]))

#find xmas in columns
for i in range(len(inputStrings[0])):
    column = ""
    for j in range(len(inputStrings)):
        column += inputStrings[j][i]
    matches += len(re.findall(pattern, column))


#find xmas in diagonals
#create upper left side diagonals
for i in range(len(inputStrings[0])):
    diagonal = ""
    for j in range(len(inputStrings)):
        if i + j < len(inputStrings[0]):
            diagonal += inputStrings[j][i + j]
    matches += len(re.findall(pattern, diagonal))

#create lower left side diagonals starting from the second row
for i in range(1, len(inputStrings)):
    diagonal = ""
    for j in range(len(inputStrings[0])):
        if i + j < len(inputStrings):
            diagonal += inputStrings[i + j][j]
    matches += len(re.findall(pattern, diagonal))

#create right side diagonals
for i in range(len(inputStrings[0])):
    diagonal = ""
    for j in range(len(inputStrings)):
        if i - j >= 0:
            diagonal += inputStrings[j][i - j]
    matches += len(re.findall(pattern, diagonal))


#create lower right side diagonals starting from the second row
for i in range(1, len(inputStrings)):  # Start from the second row
    diagonal = ""
    for j in range(len(inputStrings[0])):  # Iterate over columns
        if i + j < len(inputStrings) and j < len(inputStrings[0]):  # Stay within bounds for rows and columns
            diagonal += inputStrings[i + j][len(inputStrings[0]) - 1 - j]
    matches += len(re.findall(pattern, diagonal))

print(matches)
