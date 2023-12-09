f = open("inputs/day3.txt", "r")
lines = f.readlines()
f.close()

class coords:
    def __init__(self, value, x1, x2, y):
        self.value = value
        self.x1 = x1
        self.x2 = x2
        self.y = y



def processNum(currNums, currNum, begin, end, k):
    num = coords(currNum, begin, end, k)
    currNums.append(num)
    return currNums, -1, -1, ""



asterisks = []
nums = []
sum = 0

for k in range(len(lines)):
    line = lines[k]
    line = line.strip()
    line = [i for i in line if i]
    begin = -1
    end = -1
    currNum = ""
    nums.append([])
    currNums = nums[k]
    asterisks.append([])
    currAsterisks = asterisks[k]
    

    for i in range(len(line)):
        if line[i] == '*':
            ast = coords("*", i, i, k)
            currAsterisks.append(ast)
            if(begin != -1):
                currNums, begin, end, currNum = processNum(currNums, currNum, begin, end, k)

        elif line[i].isnumeric():
            begin = i if begin == -1 else begin
            end = i
            currNum += line[i]

        elif(begin != -1):
            currNums, begin, end, currNum = processNum(currNums, currNum, begin, end, k)

    if(begin != -1):
        currNums, begin, end, currNum = processNum(currNums, currNum, begin, end, k)
            

for i in range(len(asterisks)):
    line = asterisks[i]
    for ast in line:
        acceptableVals = [ast.x1 - 1, ast.x1, ast.x1 + 1]
        prevLine = filter(lambda num: num.x1 in acceptableVals or num.x2 in acceptableVals, 
                          nums[i-1] if i > 0 else [])
        nextLine = filter(lambda num: num.x1 in acceptableVals or num.x2 in acceptableVals, 
                            nums[i+1] if i < len(asterisks) - 1 else [])
        currLine = filter(lambda num: num.x1 == ast.x2 + 1 or num.x2 == ast.x1 - 1, nums[i])

        result = list(prevLine) + list(nextLine) + list(currLine)

        sum += int(result[0].value) * int(result[1].value) if len(result) == 2 else 0
        
print(sum)